import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions

class Vectorization:
    def __init__(self):

        self.embedding_model = SentenceTransformer("all")
        self.chroma_client - self.configure_chroma_client()
        self.collection_name = os.getenv("COLLECTION_NAME","trino_metadata_collection")
        self.embedding_functino = embedding_functions.SentenceTransformerEmbeddingFunction( model_name="all-MiniLM-Lg-v2")

    def generate_embeddings(self,query_text):

        return self.embedding_model.encode(query_text).tolist()
    
    def perform_semantic_search(self, query_text, collection_name, search_param):
        """Performs a semantic search against a ChromaDB collection."""
        if not self.chroma_client:
            raise RuntimeError("ChromaDB client not configured")
        
        try:
            # Access the correct collection
            collection = self.chroma_client.get_or_create_collection(
                name=collection_name, embedding_function=self.embedding_function
            )
            
            # Use the collection.query method for search
            results = collection.query(
                query_texts=[query_text], n_results=search_param['top_k']
            )
            return results
        except Exception as e:
            print(f"Error performing semantic search: {e}")
            return None
    
    def construct_query(self, original_sql_query, results):
        # This function remains largely the same
        if not results:
            return original_sql_query
        
        reconstructed_query = original_sql_query
        # ... logic to reconstruct query based on search results ...
        return reconstructed_query
    
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