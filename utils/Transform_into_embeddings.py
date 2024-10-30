import os
import re
import faiss
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from dotenv import load_dotenv
from langchain.docstore.document import Document as LangchainDocument
 
class TransformToEmbeddings:
    def __init__(self, processed_text):
        load_dotenv()
        self.processed_text = processed_text
 
    def get_embeddings(self):
        # Step 1: Split the text into manageable chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
        chunks = text_splitter.split_text(self.processed_text)
 
        # Step 2: Create Document objects for each chunk
        documents = [LangchainDocument(page_content=chunk, metadata={"doc_id": str(i)}) for i, chunk in enumerate(chunks)]
 
        # Step 3: Initialize the InMemoryDocstore
        docstore = InMemoryDocstore({doc.metadata['doc_id']: doc for doc in documents})
 
        # Step 4: Initialize the embeddings model
        embeddings = AzureOpenAIEmbeddings(
            openai_api_key=os.getenv('EMBEDDING_MODEL_KEY'),
            openai_api_base=os.getenv('EMBEDDING_MODEL_ENDPOINT'),
            openai_api_type=os.getenv('EMBEDDING_MODEL_TYPE'),
            deployment=os.getenv('EMBEDDING_MODEL_DEPLOYMENT_NAME'),
            api_version="2023-05-15",
        )
 
        # Step 5: Create a FAISS index for the embeddings
        index = faiss.IndexFlatL2(1536)  # 1536 is the dimensionality of the ada-002 embeddings
        vector_store = FAISS(
            embedding_function=embeddings,
            index=index,
            docstore=docstore,
            index_to_docstore_id={i: str(i) for i in range(len(documents))},
        )
 
        # Step 6: Add documents to the vector store
        vector_store.add_documents(documents)
        print('Embeddings Step Completed.')
 
        # Return the vector store and documents
        return vector_store, documents