import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os
import spacy
from pinecone import Pinecone, ServerlessSpec
from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Keys
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
PINECONE_ENVIRONMENT = os.environ["PINECONE_ENVIRONMENT"]
PINECONE_INDEX_NAME = os.environ["PINECONE_INDEX_NAME"]

# Configure pytesseract path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Initialize Cohere embeddings
embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")

# Pinecone initialization
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = os.getenv("PINECONE_INDEX_NAME")
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1024,  # Make sure this matches your embeddings' dimension
        metric='cosine',
        spec=ServerlessSpec(cloud='aws', region='us-east-1')
    )
index = pc.Index(index_name)


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


def chunk_text(text, chunk_size=500):
    """Chunk the text into smaller pieces."""
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]


def vectorize_text(text_chunks):
    """Vectorize the text chunks using Cohere embeddings."""
    return [(chunk_id, embeddings.embed_query(chunk), {"text": chunk, **metadata}) for chunk_id, chunk, metadata in text_chunks]


def upload_vectors(index, vector_data):
    """Upload vectors to Pinecone with metadata."""
    upserts = [
        {
            "id": item[0],
            "values": item[1],
            "metadata": {
                "file": item[2]["file"],
                "page": item[2]["page"],
                "chunk": item[2]["chunk"],
                "text": item[2]["text"]
            }
        }
        for item in vector_data
    ]
    index.upsert(vectors=upserts)


def process_pdf(file_path):
    """Process each PDF, extracting, preprocessing, chunking, and vectorizing text from each page, then upload to Pinecone."""
    doc = fitz.open(file_path)
    text_content = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_text = extract_text_from_page(page)
        processed_text = preprocess_text(page_text)
        chunks = chunk_text(processed_text)
        text_content.extend([(f"{file_path}_page_{page_num}_chunk_{i}", chunk, {"file": file_path, "page": page_num, "chunk": i}) for i, chunk in enumerate(chunks)])
    doc.close()

    # Vectorize and upload
    vectors = vectorize_text(text_content)
    upload_vectors(index, vectors)


def main(pdf_directory):
    """Main function to process all PDFs in the directory."""
    for root, dirs, files in os.walk(pdf_directory):
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                process_pdf(file_path)


if __name__ == "__main__":
    pdf_directory = r'F:\e-boeken\the-mystic-library\Great_Library_L-Z\Rune Magic'  # Change this to the directory containing your PDFs
    main(pdf_directory)
