
import os
import pandas as pd

from langchain.schema import Document
from langchain.retrievers.base import BaseRetriever
from typing import List
from trinoConnect import trinoConnect

from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions
import uuid 
class Vectorization:
    def __init__(self,uri,data_collection_name,metadata_collection_name):

        self.embedding_model = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MinilM-Lgv2")
        self.chroma_client = self.configure_chroma_client()
        self.metadata_collection = self.chroma_client.get_or_create_collection(metadata_collection_name, embedding_function=self.embedding_model)
        self.data_collection = self.chroma_client.get_or_create_collection(data_collection_name, embedding_function=self.embedding_model)
        self.chroma_uri = uri
    def generate_embeddings(self,data):

        return self.embedding_model.encode(data).tolist()
    
    
    
    def configure_chroma_client(self):
        """Configures and returns a ChromaDB client."""
        chroma_uri = chroma_uri
        try:
            # ChromaDB's API is simpler; you just instantiate the client
            client = chromadb.HttpClient(host=chroma_uri, port=8000)
            return client
        except Exception as e:
            print(f"Failed to create ChromaDB client: {e}")
            return None
    
    
    def loadData(self,data,metadata):

        documents = data.to_dict('records')
        ids = [str(uuid.uuid4()) for _ in range(len(documents))]

        self.data_collection.add(
            documents=[doc['document'] for doc in documents],
            metadatas=[doc['metadata'] for doc in documents],
            ids=ids
        )

        documents_metadata = metadata.to_dict('records')
        ids = [str(uuid.uuid4()) for _ in range(len(documents_metadata))]

        self.metadata_collection.add(
            documents=[doc['document'] for doc in documents_metadata],
            metadatas=[doc['metadata'] for doc in documents_metadata],
            ids=ids
        )

class TrinoMetadataRetriever(BaseRetriever):
    

    def init(self,host,port,user,catalog,schema):
        self.trino_client = trinoConnect(host,port,user,catalog,schema)    

    def get_trino_schema(self,catalog,schema):
        #Step 1: Connect to Trino and get the schema
        
        
        metadata = self.trino_client.mainQuery(f"SELECT table_name, column_name, data_type FROM information_schema.columns WHERE schema = {catalog_name}.{schema_name}")
        schema_df = pd.DataFrame(metadata, columns = ["table_name", "column_name", "data_type"])
        #Step 2: do the vectorization class to search chromaDB

        return schema_df
    
    def get_rawdata(self,catalog,schema,table):

        data = self.trino_client.mainQuery(f"SELECT * From {catalog}.{schema}.{table} ")
        schema_df = pd.DataFrame(data, columns = ["table_name", "column_name","data_type"])

        return schema_df


        
    