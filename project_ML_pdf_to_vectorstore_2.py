# This script is the feeder for my own project vectorizing PDFs and uploading them to Pinecone.
# Added more error handling for unreadable pdf's.
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
        metadata_config={'indexed': ['file', 'page', 'map', 'alignment', 'goal', 'purpose', 'tradition', 'practices']},  # Include additional fields
        spec=ServerlessSpec(cloud='aws', region='us-east-1')
    )
index = pc.Index(index_name)


def extract_text_from_page(page):
    """Extract text from a given page object."""
    try:
        text = page.get_text()
        if text.strip():  # If there's text, it's not a scan
            return text
        else:  # If no text, it's likely a scan
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        print(f"Error extracting text from page: {e}")
        return ""


def preprocess_text(text):
    """Preprocess the text using spaCy for NLP tasks."""
    doc = nlp(text)
    cleaned_text = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
    return ' '.join(cleaned_text)


def chunk_text(text, chunk_size=500):
    """Chunk the text into smaller pieces."""
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]


def vectorize_text(text_chunks, file_name, page_num, map_name, alignment, goal, purpose, tradition, practices):
    """Vectorize the text chunks using Cohere embeddings and add minimal metadata."""
    return [
        (f"{file_name}_page_{page_num}_chunk_{i}", embeddings.embed_query(chunk), {
            "file": file_name,
            "page": page_num,
            "map": map_name,
            "alignment": alignment,
            "goal": goal,
            "purpose": purpose,
            "tradition": tradition,
            "practices": practices
        })
        for i, chunk in enumerate(text_chunks)
    ]


def batch_upload_vectors(index, vector_data, namespace, batch_size=100):
    """Batch upload vectors to Pinecone with metadata."""
    for i in range(0, len(vector_data), batch_size):
        batch = vector_data[i:i + batch_size]
        upserts = [
            {
                "id": item[0],
                "values": item[1],
                "metadata": item[2]
            }
            for item in batch
        ]
        index.upsert(vectors=upserts, namespace=namespace)


def process_pdf(file_path, map_name, namespace, alignment, goal, purpose, tradition, practices):
    """Process each PDF, extracting, preprocessing, chunking, and vectorizing text from each page, then upload to Pinecone."""
    try:
        file_name = os.path.splitext(os.path.basename(file_path))[0]  # Extract file name without path and extension
        doc = fitz.open(file_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            page_text = extract_text_from_page(page)
            if not page_text.strip():
                print(f"Warning: No text extracted from page {page_num} of {file_path}")
                continue
            processed_text = preprocess_text(page_text)
            chunks = chunk_text(processed_text)
            vectors = vectorize_text(chunks, file_name, page_num, map_name, alignment, goal, purpose, tradition, practices)
            batch_upload_vectors(index, vectors, namespace)
        doc.close()
    except fitz.FileDataError as e:
        print(f"Failed to open file {file_path}: {e}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


def main(pdf_directory, namespace, alignment, goal, purpose, tradition, practices):
    """Main function to process all PDFs in the directory."""
    for root, dirs, files in os.walk(pdf_directory):
        map_name = os.path.basename(root)  # Extract map name from directory structure
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                process_pdf(file_path, map_name, namespace, alignment, goal, purpose, tradition, practices)


if __name__ == "__main__":
    pdf_directory = r'F:\e-boeken\the-mystic-library\Great_Library_H-K\Hans Jonas - The Gnostic Religion'  # Change this to the directory containing your PDFs
    namespace = "gnostics"
    alignment = "dualism anti-materialism hidden knowledge divine spark spiritual awakening"
    goal = "attain gnosis reunite divine spark god transcend material world achieve spiritual liberation"
    purpose = "expose illusory nature reality reveal path enlightenment free souls cycle of reincarnation"
    tradition = "syncretic judeo-christian roots platonic neoplatonic influences mystery religions esoteric wisdom"
    practices = "ritual magic theurgy liturgy asceticism baptism eucharist meditation mystical union"
    main(pdf_directory, namespace, alignment, goal, purpose, tradition, practices)
