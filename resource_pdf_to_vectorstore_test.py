import fitz
import pytesseract
from PIL import Image
import os
import spacy
from pinecone import Pinecone, ServerlessSpec
from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv
import logging

class PDFVectorizer:
    def __init__(self):
        load_dotenv()
        self.setup_logging()
        self.load_environment_variables()
        self.setup_nlp()
        self.setup_embeddings()
        self.setup_pinecone()

    def setup_logging(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def load_environment_variables(self):
        self.PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
        self.PINECONE_ENVIRONMENT = os.environ["PINECONE_ENVIRONMENT"]
        self.PINECONE_INDEX_NAME = os.environ["PINECONE_INDEX_NAME"]
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def setup_nlp(self):
        self.nlp = spacy.load("en_core_web_sm")

    def setup_embeddings(self):
        self.embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")

    def setup_pinecone(self):
        self.pc = Pinecone(api_key=self.PINECONE_API_KEY)

    def create_pinecone_index(self, index_name, dimension=1024):
        if index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=index_name,
                dimension=dimension,
                metric='cosine',
                metadata_config={'indexed': ['file', 'page']},
                spec=ServerlessSpec(cloud='aws', region='us-east-1')
            )
        return self.pc.Index(index_name)

    def extract_text_from_page(self, page):
        try:
            text = page.get_text()
            if text.strip():
                return text
            else:
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                text = pytesseract.image_to_string(img)
                return text
        except Exception as e:
            self.logger.error(f"Error extracting text from page: {e}")
            return ""

    def preprocess_text(self, text):
        text = ''.join(char for char in text if ord(char) >= 32 or char == '\n')
        doc = self.nlp(text)
        cleaned_sentences = [' '.join([token.text for token in sent if not token.is_space]) for sent in doc.sents]
        return ' '.join(filter(None, cleaned_sentences))

    def chunk_text(self, text, chunk_size=1000):
        words = text.split()
        return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    def vectorize_text(self, text_chunks, file_name, page_num):
        return [
            (f"{file_name}_page_{page_num}_chunk_{i}",
             self.embeddings.embed_query(chunk),
             {
                "text": chunk,
                "file": file_name,
                "page": page_num
             })
            for i, chunk in enumerate(text_chunks)
        ]

    def batch_upload_vectors(self, index, vector_data, namespace, batch_size=100):
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

    def process_pdf(self, file_path, index, namespace):
        try:
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            with fitz.open(file_path) as doc:
                for page_num in range(len(doc)):
                    page = doc.load_page(page_num)
                    page_text = self.extract_text_from_page(page)
                    if not page_text.strip():
                        self.logger.warning(f"No text extracted from page {page_num} of {file_path}")
                        continue
                    processed_text = self.preprocess_text(page_text)
                    chunks = self.chunk_text(processed_text)
                    vectors = self.vectorize_text(chunks, file_name, page_num)
                    self.batch_upload_vectors(index, vectors, namespace)
            self.logger.info(f"Successfully processed {file_path}")
        except fitz.FileDataError as e:
            self.logger.error(f"Failed to open file {file_path}: {e}")
        except Exception as e:
            self.logger.error(f"Error processing file {file_path}: {e}")

    def process_directory(self, pdf_directory, index_name, namespace):
        index = self.create_pinecone_index(index_name)
        for root, dirs, files in os.walk(pdf_directory):
            for file in files:
                if file.endswith('.pdf'):
                    file_path = os.path.join(root, file)
                    self.logger.info(f"Processing: {file_path}")
                    self.process_pdf(file_path, index, namespace)

def main():
    vectorizer = PDFVectorizer()
    pdf_directory = r'F:\e-boeken\the-mystic-library\Mystic_Library_A_Z\Left-Hand Path - LHP'
    index_name = vectorizer.PINECONE_INDEX_NAME
    namespace = "left hand path"
    vectorizer.process_directory(pdf_directory, index_name, namespace)

if __name__ == "__main__":
    main()
