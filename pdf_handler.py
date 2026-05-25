import PyPDF2
from PyPDF2.errors import PdfReadError

def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        if pdf_reader.is_encrypted:
            return "Error: This PDF is encrypted or password-protected. Please upload an unlocked PDF."

        text = ""
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"

        if not text.strip():
            return "Error: The PDF appears to be empty or contains only unreadable images/scans."

        return text.strip()

    except PdfReadError:
        return "Error: The uploaded file is corrupted or not a valid PDF document."
    except Exception as e:
        return f"Error extracting PDF: An unexpected error occurred ({str(e)})."