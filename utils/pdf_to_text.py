import fitz  # PyMuPDF
import re
class PDFEmbeddingProcessor:
   def __init__(self, pdf_path):
       """
       Initialize the processor with a PDF path.
       """
       self.pdf_path = pdf_path
       self.text = self.extract_text_from_pdf()
   def extract_text_from_pdf(self):
       """
       Extract text from the PDF file.
       """
       doc = fitz.open(self.pdf_path)
       text = ""
       for page in doc:
           text += page.get_text()
       return text
   def preprocess_text(self, text):
       """
       Preprocess the extracted text.
       """
       # Replace line breaks followed by bullets with spaces
       processed_text = re.sub(r'\n•\n', ' • ', text)
       # Remove leading and trailing spaces
       processed_text = processed_text.strip()
       # Replace multiple spaces with a single space
       processed_text = re.sub(r'\s+', ' ', processed_text)
       return processed_text
   def split_sections(self, text):
       """
       Split the text into sections based on section headers.
       """
       sections = re.split(r'\n([A-Za-z &]+)\n', text)
       # Remove empty strings from the list
       sections = [section.strip() for section in sections if section.strip()]
       formatted_text = {}
       for i in range(0, len(sections), 2):
           section_name = sections[i]
           section_content = sections[i + 1] if i + 1 < len(sections) else ""
           formatted_text[section_name] = section_content.split(' • ')
       return formatted_text
   def format_text(self, formatted_text):
       """
       Format the text into a structured format.
       """
       output = ""
       for section, items in formatted_text.items():
           output += f"### {section}\n\n"
           for item in items:
               if item.strip():
                   output += f"- {item.strip()}\n"
           output += "\n"
       return output
   def process_text(self):
       """
       Preprocess and format the text.
       """
       processed_text = self.preprocess_text(self.text)
       formatted_text = self.split_sections(processed_text)
       output = self.format_text(formatted_text)
       return output