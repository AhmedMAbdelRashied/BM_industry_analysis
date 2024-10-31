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
from app.EnumIndustryName import IndustryName
from banque_misr_industry_analysis.industry_data import industry_data
from utils.helper_functions import read_ymal
from app.EnumIndustryName import IndustryName
from datetime import datetime 


class IndustryAnalysisModule():
    def __init__(self,
                 industries_queries_path='config/queries.yml',
                 industries_prompts_path='config/prompts.yml'
                 ) -> None:
        
        # Get the current date
        self.today = datetime.today()
        # Format the date as 'day month year'
        self.date_string = self.today.strftime("%d-%B-%Y") 

        # Prompts and File paths
        self.industries_queries_path=industries_queries_path
        self.industries_prompts_path=industries_prompts_path

    def get_industries_data(self) -> list[dict] :

        industries_queries=read_ymal(self.industries_queries_path)
        industries_prompts=read_ymal(self.industries_prompts_path)
        return industries_prompts, industries_queries

    def process_bing_query(self,bing, query):
        try:
            return bing.pipeline(query)
        except Exception as e:
            print(f"\n---------------------\nError fetching Bing results for query '{query}'\n: Error: {e}\n---------------------\n")
            return None
    
    # Function to process a single prompt asynchronously
    def process_prompt(
            self,
            openai_service,
            bing,
            vector_store,
            selected_language,
            prompt_key,
            prompt_data
        ):

        # Get the current date
        # Format the date as 'day month year'

        # Current year
        current_year = int(self.today.strftime("%Y"))
        # - note that today's date is {date_string} anything beyond add it as forcasting
    
        print(f"\n---------------------\nProcessing {prompt_key}\n---------------------\n")
        prompt = prompt_data["prompt"]

        """ 
            Replace dynamic variables stored in prompt
            p means current year (+) the number after the (_)
            m means current year (-) the number after the (_)

        """
        prompt = prompt.format(
                current_year=current_year,
                date_string=self.date_string,
                # replace next years
                current_year_p_1=current_year+1,
                current_year_p_2=current_year+2,
                current_year_p_3=current_year+3,
                current_year_p_4=current_year+4,
                current_year_p_5=current_year+5,
                # replace previous years
                current_year_m_1=current_year-1,
                current_year_m_2=current_year-2,
                current_year_m_3=current_year-3,
                current_year_m_4=current_year-4,
                current_year_m_5=current_year-5,
            )
        

        # Replace the [language] placeholder with the selected language
        prompt = prompt.replace("[language]", selected_language)
    
        #run the F string function to replace all dynamic variables

        bing_query_list = prompt_data.get("bing_query", None)
        bing_results = []
 
        if bing_query_list:
            # Use ThreadPoolExecutor to process Bing queries concurrently
            with ThreadPoolExecutor(max_workers = 10) as bing_executor:
                future_to_query = {
                    bing_executor.submit(self.process_bing_query, bing, query): query
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


    def load_embeddings(self,industry_name):
        return PDFEmbeddingProcessorSaver.load_embeddings(IndustryName.get_value(industry_name))

    def create_industry_analysis(
                            self,
                            language:str,
                            industry_name:str,
                            ):
    
    
        # read industries data
        industries_prompts, industries_queries=self.get_industries_data()


        if industry_name not in industries_prompts.keys():
            return 'this industry not found !'
    
        pdf_paths=industries_prompts[industry_name]['pdf']
        prompts={key:value for key,value in industries_prompts[industry_name].items() if key != 'pdf'}
        
        keys=prompts.keys()
        keys = list(keys)
        for section in keys:
            if prompts[section]['bing_query']:
                prompts[section]['bing_query']=industries_queries[industry_name][section]
            else:
                prompts[section]['bing_query']=None
        bing = BingSearch()
        openai_service = AzureOpenAIService()
        filename = f"{industry_name}_report-{self.date_string}.docx"
        output_file_path = f'output/{filename}'
        doc_formatter = DocumentFormatter(output_file_path, language)
        # Load embeddings for the selected industry
        vector_store, documents = self.load_embeddings(industry_name)
        # Process prompts concurrently
        responses = []
        with ThreadPoolExecutor() as executor:
            future_to_prompt = {
                executor.submit(
                    self.process_prompt,
                    openai_service,
                    bing,
                    vector_store,
                    language,
                    prompt_key,
                    prompt_data
                ): (prompt_key, prompt_data)
                for prompt_key, prompt_data in prompts.items() if prompt_key != 'pdf'
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
        return filename



    
    