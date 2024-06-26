# Pdf-extraction-to-vector-storage

This project is a Python-based solution for extracting text from PDF files, preprocessing the text, vectorizing it using Cohere embeddings, and storing the vectors in Pinecone for further use.

## Workflow Breakdown

1. **Initialization**: The script begins by initializing the necessary libraries. These include:
   - PyMuPDF for PDF processing
   - pytesseract for Optical Character Recognition (OCR)
   - spaCy for Natural Language Processing (NLP)
   - Cohere for generating text embeddings
   - Pinecone for vector storage

2. **Text Extraction**: The `extract_text_from_page` function is responsible for extracting text from each page of the PDF. It uses PyMuPDF for text extraction and Tesseract for OCR in case the page contains scanned images.

3. **Text Preprocessing**: The `preprocess_text` function uses spaCy to normalize and clean the extracted text. The `chunk_text` function then divides the cleaned text into smaller pieces for efficient processing.

4. **Vectorization**: The `vectorize_text` function takes the preprocessed text chunks and generates vector embeddings using the Cohere model.

5. **Upload to Pinecone**: The `upload_vectors` function takes the generated vectors and uploads them to a Pinecone index for storage and retrieval.

6. **Process PDF**: The `process_pdf` function orchestrates the entire workflow for each PDF file. It extracts, preprocesses, and vectorizes the text from each page, and then uploads the vectors to Pinecone.

7. **Main Function**: The `main` function serves as the entry point of the script. It iterates through a specified directory, identifies all PDF files, and processes each one using the `process_pdf` function.

## Usage

To use this script, specify the directory containing your PDF files in the `main` function and run the script. Ensure that all necessary environment variables are set in your `.env` file.