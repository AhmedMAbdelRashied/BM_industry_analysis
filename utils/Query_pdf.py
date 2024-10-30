import os
import openai
from dotenv import load_dotenv
from datetime import datetime 

# Get the current date
today = datetime.today()
# Format the date as 'day month year'
date_string = today.strftime("%d-%B-%Y")

class AzureOpenAIService:
    def __init__(self):
        # Load environment variables
        load_dotenv()
 
        # Initialize environment variables
        self.api_type = os.getenv('OPEN_AI_TYPE')
        self.api_base = os.getenv('AZURE_OPENAI_ENDPOINT')  # API base URL
        self.api_version = "2024-06-01"
        self.api_key = os.getenv('OPENAI_API_KEY')  # API key
        self.deployment_name = os.getenv('OPEN_AI_DEPLOYMENT_NAME')  # Deployment name
 
        # Set OpenAI API credentials
        openai.api_type = self.api_type
        openai.api_base = self.api_base
        openai.api_version = self.api_version
        openai.api_key = self.api_key
 
        # Initialize the AzureOpenAI client
        self.client = openai.AzureOpenAI(api_key=self.api_key,api_version = self.api_version)
 
    def query_pdf(self, prompt, language):
        max_response_tokens = 4096
 
        # System prompt
        system_prompt = f"""You are an experienced industry analyst tasked with generating an industry report based on user requests, only in {language}. Be specific, detail-oriented, and include as much information as possible.
        - Use the provided context as your primary source of information. Ensure that your answer is accurate, detailed, informative, and up to date.
        - note that today's date is {date_string} anything beyond add it as forcasting
        - Make sure your report doesn't contain any contradictions.
        - Your response must be detailed and as long as possible.
        - Please note that no responses are disallowed, as this is research that will inform decision-making, so it must be transparent.
        """
        
        try:
            # Make the API request
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_response_tokens,
                temperature=0,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
 
            # Extract the response content
            answer = response.choices[0].message.content
 
        except openai.APIError as e:
            # Handle all API-related errors
            answer = f"Query_PDF Response Model API Error: {e}"
 
        except openai.APIConnectionError as e:
            # Handle connection errors
            answer = f"Query_PDF Response Model Connection Error: {e}"
        
        except openai.RateLimitError as e:
            # Handle rate-limiting errors
            answer = f"Query_PDF Response Model Rate Limit Error: {e}"
        
        except openai.BadRequestError as e:
            # Handle bad request errors (InvalidRequestError was renamed)
            answer = f"Query_PDF Response Model Bad Request: {e}"
        
        except openai.AuthenticationError as e:
            # Handle authentication errors
            answer = f"Query_PDF Response Model Authentication Error: {e}"
        
        except Exception as e:
            # General exception handling
            answer = f"Query_PDF Response Model An error occurred: {e}"
 
        return answer