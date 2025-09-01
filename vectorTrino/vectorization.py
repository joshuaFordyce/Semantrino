
import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions

class Vectorization:
    def __init__(self):

        self.embedding_model = SentenceTransformer("all")
        self.chroma_client - self.configure_chroma_client()
        self.collection_name = os.getenv("COLLECTION_NAME","trino_metadata_collection")
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction( model_name="all-MiniLM-Lg-v2")

    def generate_embeddings(self,data):

        return self.embedding_model.encode(query_text).tolist()
    
    
    
    def configure_chroma_client(self):
        """Configures and returns a ChromaDB client."""
        chroma_uri = os.getenv("CHROMA_URI", "http://localhost:8000")
        try:
            # ChromaDB's API is simpler; you just instantiate the client
            client = chromadb.HttpClient(host=chroma_uri, port=8000)
            return client
        except Exception as e:
            print(f"Failed to create ChromaDB client: {e}")
            return None
    def loadData(self,data,metadata):
        self.collection_name.add(documents=data,)