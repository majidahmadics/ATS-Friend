import pdfplumber
from typing import IO

class PDFParser:
    """
    A class to handle PDF parsing using pdfplumber.
    """
    
    @staticmethod
    def extract_text_from_pdf(pdf_file: IO) -> str:
        """
        Extracts text from a PDF file using pdfplumber.
        
        Args:
            pdf_file (IO): A file-like object representing the PDF file.
        
        Returns:
            str: The extracted text from the PDF.
        """
        try:
            with pdfplumber.open(pdf_file) as pdf:
                text_content = ""
                for page in pdf.pages:
                    text_content += page.extract_text() or ""
                return text_content
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return ""