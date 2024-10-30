import os
import pickle
import faiss
from utils.pdf_to_text import PDFEmbeddingProcessor
from utils.Transform_into_embeddings import TransformToEmbeddings
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
 
class PDFEmbeddingProcessorSaver:
    def __init__(self, pdf_dir, output_dir='raw_data_vector_store'):
        self.pdf_dir = pdf_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
 
    def get_pdf_paths(self):
        if isinstance(self.pdf_dir, str) and os.path.isdir(self.pdf_dir):
            return [os.path.join(self.pdf_dir, f) for f in os.listdir(self.pdf_dir) if f.endswith('.pdf')]
        return []
 
    def process_and_save_embeddings(self, industry_name):
        pdf_paths = self.get_pdf_paths()
        if not pdf_paths:
            print(f"No PDFs found for '{industry_name}'. Skipping PDF processing.")
            return
 
        all_processed_texts = ""
        for pdf_path in pdf_paths:
            processor = PDFEmbeddingProcessor(pdf_path)
            processed_text = processor.process_text()
            all_processed_texts += processed_text + "\n\n"
 
        transformer = TransformToEmbeddings(all_processed_texts)
        vector_store, documents = transformer.get_embeddings()
 
        # Save components separately
        index_filename = os.path.join(self.output_dir, f"{industry_name}_faiss_index.pkl")
        documents_filename = os.path.join(self.output_dir, f"{industry_name}_documents.pkl")
        docstore_filename = os.path.join(self.output_dir, f"{industry_name}_docstore.pkl")
 
        # Save FAISS index
        faiss.write_index(vector_store.index, index_filename)
 
        # Save documents
        with open(documents_filename, 'wb') as docs_file:
            pickle.dump(documents, docs_file)
 
        # Save docstore
        with open(docstore_filename, 'wb') as docstore_file:
            pickle.dump(vector_store.docstore._dict, docstore_file)
 
        print(f"Embeddings for '{industry_name}' saved to {self.output_dir}.")
 
    @staticmethod
    def load_embeddings(industry_name, output_dir='raw_data_vector_store'):
        index_filename = os.path.join(output_dir, f"{industry_name}_faiss_index.pkl")
        documents_filename = os.path.join(output_dir, f"{industry_name}_documents.pkl")
        docstore_filename = os.path.join(output_dir, f"{industry_name}_docstore.pkl")
 
        if not all(os.path.exists(f) for f in [index_filename, documents_filename, docstore_filename]):
            print(f"\n---------------------\nNo embeddings found for industry '{industry_name}'. Skipping vector store loading.\n---------------------\n")
            return None, None
 
        # Load FAISS index
        index = faiss.read_index(index_filename)
 
        # Load documents
        with open(documents_filename, 'rb') as docs_file:
            documents = pickle.load(docs_file)
 
        # Load docstore
        with open(docstore_filename, 'rb') as docstore_file:
            docstore_dict = pickle.load(docstore_file)
 
        # Recreate the docstore
        docstore = InMemoryDocstore(docstore_dict)
 
        # Recreate the vector store
        embeddings = AzureOpenAIEmbeddings(
            openai_api_key=os.getenv('EMBEDDING_MODEL_KEY'),
            openai_api_base=os.getenv('EMBEDDING_MODEL_ENDPOINT'),
            openai_api_type=os.getenv('EMBEDDING_MODEL_TYPE'),
            deployment=os.getenv('EMBEDDING_MODEL_DEPLOYMENT_NAME'),
            api_version="2023-05-15",
        )
 
        vector_store = FAISS(
            embedding_function=embeddings,
            index=index,
            docstore=docstore,
            index_to_docstore_id={i: str(i) for i in range(len(documents))},
        )
 
        return vector_store, documents