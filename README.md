## Pdf-extraction-to-vector-storage
# Breakdown
### Initialization: The script initializes the necessary libraries, including PyMuPDF, pytesseract, spaCy, Cohere embeddings, and Pinecone.
### Text Extraction: The function extract_text_from_page handles the extraction of text from PDFs using PyMuPDF and Tesseract for OCR.
### Text Preprocessing: The preprocess_text function uses spaCy to normalize and clean the text, and the chunk_text function divides it into smaller pieces.
### Vectorization: The vectorize_text function generates vector embeddings using Cohere.
### Upload to Pinecone: The upload_vectors function uploads the vectors to Pinecone.
### Process PDF: The process_pdf function orchestrates the entire workflow for each PDF file.
### Main Function: The main function iterates through the specified directory and processes each PDF.