import io
import time
from datetime import datetime
import os
import pickle
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.PDFEmbeddingProcessorSaver import PDFEmbeddingProcessorSaver
from utils.Bing_search import BingSearch
from utils.Summarize_with_gpt import SummarizeWithGPT
from utils.Transform_into_embeddings import TransformToEmbeddings
from utils.Query_pdf import AzureOpenAIService
from utils.Doc_creation import DocumentFormatter
from banque_misr_industry_analysis.EnumIndustryName import IndustryName
from banque_misr_industry_analysis.industry_data import industry_data
from helper_functions.helper_functions import *
# Get the current date
today = datetime.today()
# Format the date as 'day month year'
date_string = today.strftime("%d-%B-%Y") 


from flask import Flask



app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
industries_names_path='config\industryName.txt'
industries_queries_path='config\queries.yml'
industries_prompts_path='config\prompts.yml'



industries_names=read_txt(industries_names_path)
industries_queries=read_ymal(industries_queries_path)
industries_prompts=read_ymal(industries_prompts_path)


def get_industries_name():
    return industries_prompts.keys()

# Function to process a single Bing query asynchronously
def process_bing_query(bing, query):
    try:
        return bing.pipeline(query)
    except Exception as e:
        print(f"\n---------------------\nError fetching Bing results for query '{query}'\n: Error: {e}\n---------------------\n")
        return None
# Function to process a single prompt asynchronously
def process_prompt(openai_service, bing, vector_store, selected_language, prompt_key, prompt_data):

    print(f"\n---------------------\nProcessing {prompt_key}\n---------------------\n")
    prompt = prompt_data["prompt"]
    # Replace the [language] placeholder with the selected language
    prompt = prompt.replace("[language]", selected_language)
 
    bing_query_list = prompt_data.get("bing_query", None)
    bing_results = []
 
    if bing_query_list:
        # Use ThreadPoolExecutor to process Bing queries concurrently
        with ThreadPoolExecutor(max_workers = 10) as bing_executor:
            future_to_query = {
                bing_executor.submit(process_bing_query, bing, query): query
                for query in bing_query_list
            }
 
            # Collect results as they complete
            for future in as_completed(future_to_query):
                result = future.result()
                if result:
                    bing_results.append(result)
 
    # Combine all Bing query results
    combined_news = "\n\n".join(bing_results) if bing_results else None

    context = ""
    # Combine Context and Prompt for openai
    if vector_store:
        # Retrieve relevant chunks from the vector store
        relevant_docs = vector_store.similarity_search(prompt, k=10)
        context += " ".join([doc.page_content for doc in relevant_docs]) 
    if combined_news:
        context += f'\nLatest News: {combined_news}'
    
    # Combine the context with the question
    question = f"Context: {context}\n\nTask: {prompt}"
   
    # Generate response using Azure OpenAI's query_pdf method
    response = openai_service.query_pdf(question, selected_language)
    print(f"\n---------------------\nSucess {prompt_key} is done\n---------------------\n")
    return (prompt_key, response)


def load_embeddings(industry_name):
    return PDFEmbeddingProcessorSaver.load_embeddings(industry_name)
 

def create_industry_analysis(language:str,industry_name:str):
    
    # Record the start time
    start_time = time.time()
    if industry_name not in industries_prompts.keys():
        return 'this industry not found !'
    pdf_paths=industries_prompts['pdf_paths']
    prompts={key:value for key,value in industries_prompts if key != 'pdf_paths'}
    
    for section in prompts.keys():
        if prompts[section]['bing_query']:
            prompts[section]['bing_query']=industries_queries[industry_name][section]
        else:
            prompts[section]['bing_query']=None
    bing = BingSearch()
    openai_service = AzureOpenAIService()
    filename = f"{industry_name.replace}_report-{date_string}.docx"
    output_file_path = f'output/{filename}'
    doc_formatter = DocumentFormatter(output_file_path, language)
    # Load embeddings for the selected industry
    vector_store, documents = load_embeddings(industry_name)
    # Process prompts concurrently
    responses = []
    with ThreadPoolExecutor() as executor:
        future_to_prompt = {
            executor.submit(
                process_prompt, openai_service, bing, vector_store, selected_language, prompt_key, prompt_data
            ): (prompt_key, prompt_data)
            for prompt_key, prompt_data in prompts.items()
        }
 
        # Collect results as they complete, ensuring correct order
        for future in as_completed(future_to_prompt):
            prompt_key, response = future.result()
            responses.append((prompt_key, response))
    # Sort responses to ensure they are in the correct order
    responses.sort(key=lambda x: list(prompts.keys()).index(x[0]))
 
    # Combine all responses into a single string
    combined_responses = "\n\n".join([response for _, response in responses])
 
    # Add the combined responses to the document
    doc_formatter.add_text_to_doc(combined_responses)
 
    # Save the final document after all prompts have been processed
    doc_formatter.save()

# Record the end time
    end_time = time.time()
 
    # Calculate the duration in seconds
    total_time_taken = end_time - start_time
 
    # Convert the time to minutes
    total_time_taken_minutes = total_time_taken / 60
@app.route("/")
def home():
    create_industry_analysis("arabic",'Oil and Gas')
    return " Done"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)