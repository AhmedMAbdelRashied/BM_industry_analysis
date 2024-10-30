import os
import re
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from utils.Summarize_with_gpt import SummarizeWithGPT
import concurrent.futures
from datetime import datetime 
import warnings
warnings.filterwarnings("ignore")
 
# Get the current date
today = datetime.today()
date_string = today.strftime("%d-%B-%Y")  # Format the date as 'day month year'

class BingSearch:
    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()
        
        # Bing Search API credentials
        self.bing_subscription_key = os.getenv('bing_subscription_key')
        self.bing_search_url = os.getenv('bing_search_url')
        
        # Azure OpenAI credentials
        self.azure_openai_api_key = os.getenv('OPENAI_API_KEY')
        self.azure_openai_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
        self.azure_openai_model = "gpt-4o"
        self.azure_openai_deployment = os.getenv('OPEN_AI_DEPLOYMENT_NAME')
        self.openai_api_version = os.getenv('AZURE_OPENAI_VERSION')
        self.api_type = os.getenv('OPEN_AI_TYPE')
 
    # Step 1: Fetch real-time data from Bing Search
    def search_bing(self, query, top_results=20):
        headers = {"Ocp-Apim-Subscription-Key": self.bing_subscription_key}
        params = {
            "q": f'{query} {date_string}',
            "textDecorations": True,
            "textFormat": "HTML",
            "count": top_results  # Limit results to top 'n' results
        }
        try:
            response = requests.get(
                self.bing_search_url,
                headers=headers,
                params=params,
                verify=False
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during Bing search: {e}")
            return {}
 
    # Step 2: Retrieve content from a single URL
    def retrieve_url_content(self, url):
        try:
            response = requests.get(url, timeout=1)
            response.raise_for_status()
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract the main text content from the webpage
            paragraphs = soup.find_all('p')
            content = " ".join([p.get_text() for p in paragraphs])
            return content[:2000]  # Limit to 2000 characters to avoid token overflow
        except Exception as e:
            # Optionally log the error
            #print(f"Failed to retrieve content from {url}: {e}")
            return None  # Return None if content retrieval fails
 
    # Step 3: Parse the search results and fetch content from URLs in parallel
    def parse_and_fetch_content(self, search_results):
        parsed_data = []
        urls = [
            {
                "title": result.get("name", "No Title"),
                "snippet": result.get("snippet", "No Description"),
                "url": result.get("url", "No URL")
            }
            for result in search_results.get("webPages", {}).get("value", [])
        ]
        
        # Use ThreadPoolExecutor for I/O-bound operations
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Create a future for each URL content retrieval
            future_to_url = {
                executor.submit(self.retrieve_url_content, item['url']): item
                for item in urls
            }
            for future in concurrent.futures.as_completed(future_to_url):
                item = future_to_url[future]
                try:
                    url_content = future.result()
                    if url_content:
                        # Combine title, description, and fetched content
                        parsed_data.append({
                            "title": item['title'],
                            "snippet": item['snippet'],
                            "content": url_content,
                            "url": item['url']
                        })
                except Exception as e:
                    # Optionally log the exception
                    #print(f"Error processing URL {item['url']}: {e}")
                    continue  # Skip this URL on failure
        
        return parsed_data
 
    # Step 4: Enhance keyword search using re-rank mechanism
    def re_rank_content(self, parsed_data, query):
        # Tokenize the query into keywords (lowercase for case insensitivity)
        # Use unicode-aware regular expression for English and Arabic queries
        query_keywords = re.findall(r'\w+', query.lower(), re.UNICODE)
        scored_data = []
        for data in parsed_data:
            # Tokenize the content (lowercase for case insensitivity)
            content = data['content'].lower()
            # Count occurrences of each keyword in the content
            score = sum(content.count(keyword) for keyword in query_keywords)
            # Store the data along with its relevance score
            scored_data.append({
                "title": data['title'],
                "snippet": data['snippet'],
                "content": data['content'],
                "url": data['url'],
                "score": score
            })
        # Sort the data by score in descending order (highest relevance first)
        ranked_data = sorted(scored_data, key=lambda x: x['score'], reverse=True)
        # Combine the ranked data into a single string to send to GPT
        ranked_content = "\n".join(
            f"Title: {item['title']}\nDescription: {item['snippet']}\nContent: {item['content']}\nURL: {item['url']}\n"
            for item in ranked_data
        )
        return ranked_content
 
    # Step 5: Define the processing pipeline
    def pipeline(self, query):
        # Fetch search results from Bing
        bing_results = self.search_bing(query)
        if not bing_results:
            return "No search results found or an error occurred."
        
        # Parse the search results and retrieve content from URLs in parallel
        parsed_content = self.parse_and_fetch_content(bing_results)
        if not parsed_content:
            return "No content retrieved from the search results."
        
        # Re-rank the fetched content based on keyword relevance
        ranked_content = self.re_rank_content(parsed_content, query)
        if not ranked_content.strip():
            return "No relevant content to summarize."
        
        #return ranked_content
        # Summarize the re-ranked content using Azure OpenAI
        try:
            gpt_summary = SummarizeWithGPT()
            results = gpt_summary.summarize(ranked_content)
            return results
        except Exception as e:
            print(f"Error during summarization: {e} For the Query: {query}")
            return "An error occurred while summarizing the content."