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





     
     

class SQLQueryRequest(BaseModel):
    sql: str
    limit: int = 10

    @app.get("/")
    async def root():
        print("Please set the following environment variables:")
        print("milvus_URI, collection_name, vector_embedding, search_param")
        env_vars = Vectorization.get_env()

        return {
            "message": "SemanTrino is up and working",
            "config": env_vars
        }

    @app.get("/search")
    async def search(query_data: SQLQueryRequest):
        original_sql_query = query_data.sql
        limit = query_data.limit
    
        env_vars = Vectorization.get_env()
        client = Vectorization.configure_chroma_client()
        embeddings = Vectorization.generate_embeddings(original_sql_query)
        results = Vectorization.perform_semantic_search(client,embeddings,env_vars.get("collection_name", env_vars.get("search_param")))
        reconstructedquery = Vectorization.construct_query(original_sql_query,results)
        return reconstructedquery