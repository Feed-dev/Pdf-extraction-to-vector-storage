import pinecone
from langchain_community.embeddings import CohereEmbeddings

embeddings = CohereEmbeddings(model="multilingual-22-12")


def vectorize_text(text_chunks):
    return [(f"{chunk_id}", embeddings.embed_query(chunk)) for chunk_id, chunk in text_chunks]


# Initialize Pinecone
pinecone.init(api_key="your-pinecone-api-key", environment='us-west1-gcp')
index_name = "vector-index"

# Create or connect to an existing index
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=768, metric='cosine')  # Adjust dimension based on your embeddings
index = pinecone.Index(index_name)


# Upload vectors
def upload_vectors(index, vector_data):
    upserts = [(item[0], item[1]) for item in vector_data]
    index.upsert(vectors=upserts)
