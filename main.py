import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os

# Configure pytesseract path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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

def process_pdf(file_path):
    """Process each PDF, extracting text from each page."""
    doc = fitz.open(file_path)
    text_content = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_text = extract_text_from_page(page)
        text_content.append(page_text)
    doc.close()
    return "\n".join(text_content)

def main(pdf_directory):
    for root, dirs, files in os.walk(pdf_directory):
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                text = process_pdf(file_path)
                # Save the extracted text to a .txt file or handle as needed
                output_path = file_path.replace('.pdf', '.txt')
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(text)

if __name__ == "__main__":
    pdf_directory = r'F:\e-boeken\The Mystic Library\Great_Library_A-G\Alchemy'
    main(pdf_directory)
