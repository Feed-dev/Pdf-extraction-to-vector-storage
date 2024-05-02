import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os
import spacy

# Configure pytesseract path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


def extract_text_from_page(page):
    """Extract text from a given page object."""
    text = page.get_text()
    if text.strip():  # If there's text, it's not a scan
        return text
    else:  # If no text, it's likely a scan
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text = pytesseract.image_to_string(img)
        return text


def preprocess_text(text):
    """Preprocess the text using spaCy for NLP tasks."""
    doc = nlp(text)
    cleaned_text = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
    return ' '.join(cleaned_text)


def process_pdf(file_path):
    """Process each PDF, extracting and preprocessing text from each page."""
    doc = fitz.open(file_path)
    text_content = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_text = extract_text_from_page(page)
        # Preprocess the extracted text
        processed_text = preprocess_text(page_text)
        text_content.append(processed_text)
    doc.close()
    return "\n".join(text_content)


def main(pdf_directory):
    for root, dirs, files in os.walk(pdf_directory):
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                text = process_pdf(file_path)
                # Save the preprocessed text to a .txt file
                output_path = file_path.replace('.pdf', '.txt')
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(text)


if __name__ == "__main__":
    pdf_directory = r'C:\Library\PDF_directory'  # Change this to the directory containing your PDFs
    main(pdf_directory)
