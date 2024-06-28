import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os
import spacy
from pinecone import Pinecone, ServerlessSpec
from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv
import logging
from sklearn.metrics.pairwise import cosine_similarity

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

# Keys
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
PINECONE_ENVIRONMENT = os.environ["PINECONE_ENVIRONMENT"]
PINECONE_INDEX_NAME = os.environ["PINECONE_INDEX_NAME2"]

# Configure pytesseract path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Initialize Cohere embeddings
embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")

# Pinecone initialization
pc = Pinecone(api_key=PINECONE_API_KEY)

def create_pinecone_index(index_name, dimension=1024):
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric='cosine',
            metadata_config={'indexed': ['file', 'page', 'map', 'alignment', 'goal', 'purpose', 'tradition', 'practices']},
            spec=ServerlessSpec(cloud='aws', region='us-east-1')
        )
    return pc.Index(index_name)

def extract_text_from_page(page):
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
        logger.error(f"Error extracting text from page: {e}")
        return ""


def preprocess_text(text):
    # Remove Unicode escape sequences and non-printable characters
    text = ''.join(char for char in text if ord(char) >= 32 or char == '\n')

    doc = nlp(text)
    cleaned_sentences = []
    for sent in doc.sents:
        # Keep original capitalization and punctuation
        cleaned_words = [token.text for token in sent if not token.is_space]
        cleaned_sentence = ' '.join(cleaned_words)
        if cleaned_sentence:
            cleaned_sentences.append(cleaned_sentence)

    return ' '.join(cleaned_sentences)

def chunk_text(text, chunk_size=1000):
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

def semantic_similarity(query_embedding, document_embedding):
    return cosine_similarity([query_embedding], [document_embedding])[0][0]

def vectorize_text(text_chunks, file_name, page_num, metadata, query_embedding):
    return [
        (f"{file_name}_page_{page_num}_chunk_{i}",
         chunk_embedding,
         {
            "text": chunk,
            "file": file_name,
            "page": page_num,
            "similarity_score": semantic_similarity(query_embedding, chunk_embedding),
            **metadata
         })
        for i, chunk in enumerate(text_chunks)
        for chunk_embedding in [embeddings.embed_query(chunk)]
    ]

def batch_upload_vectors(index, vector_data, namespace, batch_size=100):
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

def process_pdf(file_path, index, namespace, metadata, query_embedding):
    try:
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        doc = fitz.open(file_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            page_text = extract_text_from_page(page)
            if not page_text.strip():
                logger.warning(f"No text extracted from page {page_num} of {file_path}")
                continue
            processed_text = preprocess_text(page_text)
            chunks = chunk_text(processed_text)
            vectors = vectorize_text(chunks, file_name, page_num, metadata, query_embedding)
            batch_upload_vectors(index, vectors, namespace)
        doc.close()
        logger.info(f"Successfully processed {file_path}")
    except fitz.FileDataError as e:
        logger.error(f"Failed to open file {file_path}: {e}")
    except Exception as e:
        logger.error(f"Error processing file {file_path}: {e}")

def main(pdf_directory, index_name, namespace, metadata, query):
    index = create_pinecone_index(index_name)
    query_embedding = embeddings.embed_query(query)
    for root, dirs, files in os.walk(pdf_directory):
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                logger.info(f"Processing: {file_path}")
                process_pdf(file_path, index, namespace, metadata, query_embedding)

if __name__ == "__main__":
    # Example usage for a small test index
    test_pdf_directory = r'F:\e-boeken\the-mystic-library\Mystic_Library_A_Z\Astral Workings'
    test_index_name = PINECONE_INDEX_NAME
    test_namespace = "astral workings"
    test_metadata = {
        "map": "astral-workings",
        "alignment": "spiritual development",
        "goal": "explore inner self",
        "purpose": "astral projection",
        "tradition": "esoteric",
        "practices": "meditation, visualization"
    }
    sample_query = "What is astral projection?"
    main(test_pdf_directory, test_index_name, test_namespace, test_metadata, sample_query)
