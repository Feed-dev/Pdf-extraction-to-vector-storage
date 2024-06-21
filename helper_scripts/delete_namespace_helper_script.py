import os
from pinecone import Pinecone
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def delete_namespace(api_key, index_name, namespace):
    # Initialize Pinecone
    pc = Pinecone(api_key=api_key)

    # Connect to the Pinecone index
    index = pc.Index(index_name)

    # Delete all vectors in the specified namespace
    index.delete(delete_all=True, namespace=namespace)
    print(f"Namespace '{namespace}' successfully deleted.")


if __name__ == "__main__":
    # Load Pinecone API key and index name from environment variables
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX_NAME")

    # Set the namespace you want to delete
    namespace_to_delete = "hermeticism"

    delete_namespace(api_key, index_name, namespace_to_delete)
