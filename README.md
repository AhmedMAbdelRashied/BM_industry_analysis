#Module Descriptions:


banque_misr_industry_analysis/

            --EnumIndustryName.py
                is used by the main.py file to select the industry name as it takes a number and returns the selected industry name

            --industry_data.py
                is used by the main.py file to retrieve the selected industry's fitch pdfs and prompts


prompt/



            --prompts.py
                # contains prompts for every industry (industry name as a variable contains a json list of the sections and bing_quiries)
                ## this file is used by the main.py file as it retrieve the sections and send to utils/Query_pdf.py file to process it 


utils/

        --pdf_to_text.py:
        
                ---Component to convert the pdf to txt through 3 methods : 
                        # extract_text_from_pdf()
                                ---- 1.Open the PDF
                                     2.loop over each page inside the PDF
                                     3. return extracted text 
                        # preprocess_text()     
                                ---- 1.Preprocess the extracted text from PDF
                                     2.return extracted text after preprocessing by extract_text_from_pdf()

                                
                        # split_sections()
                                ---- 1.split text into sections by specifying section headers
                                     2.return text after formating

                        # format_text()
                                ----1.takes formated text after splitting 
                                    2.return structured text
                        # process_text()
                                ----1.share preprocess_text(),split_sections(),format_text()
                                    2.return final processed text 


        --Bing_search.py
                ---Component that returns latest news to the main.py file through 7 methods:
                        # __init__()
                                1. initialize the bing api
                                2. initialize the azure openai
                        # search_bing()
                                1. search the internet by a query from the main.py file
                                2. returns the response in a json contains titles, urls and snippet of the retrieved websites
                        # retrieve_url_content()
                                1. scrap the urls that is returned from search_bing
                                2. add the scraped content to the json it now contains titles, urls, snippet and content of the websites
                        # re_rank_content() 
                                1. re rank the restults from the retrieve_url_content by keywords into only top 5 results  
                                2. returns the new re ranked list
                        # SummarizeWithGPT() from utils/Summarize_with_gpt.py file
                                1. summaraize and create a structured format of the re_rank_content results
                                2. return the summaraized content
                        # pipeline()
                                1. run the pervious functions and returns the last step gpt_summary or the (summaraized content)

                                
        --Summarize_with_gpt.py
                --- Component used by Bing_search.py to summarize and organize the scraped urls 

        --Transform_into_embeddings.py

                ---Component to transform raw structured text into embeddings TransformToEmbeddings:

                        #get_embeddings()

                                ----1.Split the text into manageable chunks 2000 chunk length
                                    2.Create Document objects for each chunk
                                    3.Initialize the InMemoryDocstore
                                    4.Initialize the embeddings model
                                    5.Create a FAISS index for the embeddings
                                    6.Add documents to the vector store
                                Return the vector store and documents
                        

        --Query_pdf.py
                --- AzureOpenAIService Component that Initializes openAI (GPT4o) model :
                        # Initialize OpenAI creditentials using 
                                        -OPEN_AI_TYPE,
                                        -AZURE_OPENAI_ENDPOINT,
                                        -AZURE_OPENAI_VERSION,
                                        -OPENAI_API_KEY,
                                        -OPEN_AI_DEPLOYMENT_NAME
                        # query_pdf() 
                                takes (vector_store ,question about the query , news_stored) 
                                ---- 1.Retrieve relevant chunks from the vector store
                                     2.Combine the context with the question
                                     3.Estimate the number of tokens in the context and question
                                     4.Ensure the total tokens do not exceed the model's limit
                                return selected answer

        

        --Doc_creation.py 
                --- document creation Component that collect all prompts output in the same doc with structure format
                        # Initialize document name()

                        # _add_initial_header()
                                1.add initial header title of our document
                        # set_paragraph_rtl()
                                1.Sets the paragraph direction to right to left specific for Arabic lan 
                        # add_text_to_doc ()
                                1.Check if the line is a table add it in the table format 
                                2.format text based on gpt output 
                                3.add text to current doc 
                        # _add_header()
                                1.Adds a header to the document with the appropriate style and font size
                        # _add_paragraph_with_bold()
                                1.Adds a paragraph with  bold formatting
                        # save()
                                1.Save document 
        --PDFEmbeddingProcessorSaver.py
                -- process_and_save_embeddings() used to generate vector store of the raw folders from industry_data.py
                -- load_embeddings used by main to load the vector store of the industry raw data



Raw_data/

        --{industry_name}/


            ---industry_name.pdf
• output/


        --{industry_report}.docx


main.py

                # get_industry_choice()
                        - Takes a number input from the user to select the industry 
        
                # main()
                        1. Gets the selected industry from the get_industry_choice
                        2. Get the industry data [prompts(indusry-prompts & bing quires) and pdfs paths]from industry_data function from banque_misr_industry_analysis/industry_data
                        3. Initialize BingSearch, AzureOpenAIService, and DocumentFormatter from utils folder
                        4. use PDFEmbeddingProcessor from utils to process the industry pdf file
                        5. loop through the industry prompts from step 2 to process every section using bing from step 3 and Query_pdf.py from utiles
                        6. save the processed word document using DocumentFormatter from step 3

preprocess_embeddings.py
        **have to be used FIRST** to run process_and_save_embeddings() in the PDFEmbeddingProcessorSaver.py to generate the vector store for all industries 