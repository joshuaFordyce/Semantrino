import chromadb

class chroma:

    def connect_to_milvus():
        try:
            connections.connect("default", host="localhost", port="19530")
            print("Connected to Milvus")
        except Exception as e:
            print(f"Failed to connect to Milvus : {e}")
            raise
    
    def create_collection(name, fields, description):
        schema = CollectionSchema(fields, description)
        collection = Collection(name, schema, consistency_level="Strong")
        return collection