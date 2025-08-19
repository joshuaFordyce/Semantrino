import os
from sentence_tranformers import SentenceTransformer
from pymilvus import MilvusClient


class Vectorization:
    def __init__(self):
    
        self.model = SentenceTransformer("all=MiniLM-L6-v2", trust_remote_code=True)
        self.client = self.configureMilvus()

    def generateEmbeddings(self,query_text):
        if not self.model:
            raise RuntimeError("SentenceTransformer model not initialized")
        vector_embedding = self.model.encode(query_text)
        return vector_embedding.tolist()

    
    
    
    def perform_semanticsearch(self,client,vector_embedding, collection_name, search_param):
        if not self.client:

            raise RuntimeError("Milvus client not configured")
        try:
            search_results = client.search(
                collection_name, vector_embedding, top_k=2, params=search_param
            )
            return search_results
        except Exception as e:
            print(f"Error performing semantic search: {e}")
            return None

    def returnllmResults():
        pass