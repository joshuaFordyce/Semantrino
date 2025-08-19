from fastapi import FastAPI,Query
import os
from fastapi.middleware.cors import CORSMiddleware
from vectorization import Vectorization
import numpy as np
from pymilvus import MilvusClient
from pydantic import BaseModel

app = FastAPI

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_env():
    milvus_uri = os.getenv("MILVUS_RUI", "http://localhost:19530")
    collection_name = os.getenv("COLLECTION_NAME","collection_name")
    search_param = os.getenv("SEARCH_PARAM", "search_param" )

    return {
        "milvus_uri" : milvus_uri,
        "collection_name": collection_name,
        "search_param" : search_param
    }
def configureMilvus():
        milvus_uri = os.getenv("MILVUS_URI", "http://localhost:19530")
        try:
            client = MilvusClient(uri=milvus_uri)
            return client
    
        except Exception as e:
            print(f"Failed to create Milvus client:{e}")
            return None
class SQLQueryRequest(BaseModel):
    sql: str
    limit: int = 10

    @app.get("/")
    async def root():
        print("Please set the following environment variables:")
        print("milvus_URI, collection_name, vector_embedding, search_param")
        env_vars = get_env

        return {
            "message": "SemanTrino is up and working",
            "config": env_vars
        }

    @app.get("/search")
    async def search(query_data: SQLQueryRequest):
        original_sql_query
    
        env_vars = get_env()
        client = configureMilvus()
        embeddings = Vectorization.generateEmbeddings()
        results = Vectorization.perform_semanticsearch(client,embeddings,env_vars.get("collection_name", env_vars.get("search_param")))
        
        return results