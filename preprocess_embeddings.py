import os
from utils.PDFEmbeddingProcessorSaver import PDFEmbeddingProcessorSaver
from banque_misr_industry_analysis.industry_data import industry_data
import warnings
warnings.filterwarnings("ignore")

def main():
# Iterate over all industries defined in industry_data.py
    for industry_name, industry_info in industry_data.items():
        pdf_dir = industry_info.get("pdf_paths")
 
        # Check if the PDF directory exists for the industry
        if not pdf_dir or not os.path.exists(pdf_dir):
            print(f"PDFs for '{industry_name}' not found in '{pdf_dir}'. Skipping this industry.")
            continue
 
        # Initialize the PDFEmbeddingProcessorSaver to process and save embeddings
        print(f"Processing embeddings for industry: {industry_name}")
        processor_saver = PDFEmbeddingProcessorSaver(pdf_dir=pdf_dir)
        processor_saver.process_and_save_embeddings(industry_name)
 
if __name__ == "__main__":
    main()