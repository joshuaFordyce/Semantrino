
from datetime import date
import json
import click
import pandas as pd
import trinoConnect

from vectorization import TrinoMetadataRetriever, Vectorization

TRINO_RETRIEVER = None
VECTOR_STORE = None



def get_retriver(config: dict) -> TrinoMetadataRetriever:
    global TRINO_RETRIEVER 
    if TRINO_RETRIEVER is None:
        trino_config = config['trino']
        TRINO_RETRIEVER = TrinoMetadataRetriever(
            trino_config['host'],
            trino_config['port'],
            trino_config['user']
        )
    return TRINO_RETRIEVER

def vector_store(config: dict) -> Vectorization:

    global VECTOR_STORE
    if VECTOR_STORE is None:
        chroma_config = config['chroma']
        VECTOR_STORE = Vectorization(
            chroma_config['uri'],
            chroma_config['rawdata_collection_name'],
            chroma_config['metadata_collection_name']
        )
    return VECTOR_STORE 

def discover_schema(retriever: TrinoMetadataRetriever, catalog: dict) -> pd.DataFrame:
    click.echo("Initializing the CLI and pulling the information schema")
    return retriever.get_trino_schema(catalog['name'], catalog['schema'])

    #with open(config_file, 'r') as f:
     #   config = json.load(f)
    #trino_config = config['trino']
    #host = trino_config['host']
    #port = trino_config['port']
    #user = trino_config['user']
    #catalogs_list = config['catalogs']

    #for catalog in catalogs_list:
     #   catalog_name = catalog['name']
      #  schema = catalog['schema']


       # trino_client = trinoConnect(host,port,user)
        #query = "SHOW tables from INFORMATION_SCHEMA"
        #trino_client.mainQuery()

    #query = "SHOW tables from Information_schema"
    #results = trino_client.mainQuery(query)
    #columns = [desc[0] for desc in results[1]]
    #df = pd.DataFrame.from_records(results[0],columns)
    #print(df)
    
    


@click.command()
@click.option(
   '--congif-file',
   '-c',
   type=click.Path(exists=True),
   required=True,
   help='Path to the Semantrino.json configuration'
)

def ingestData(vectorizer: Vectorization, metadata: pd.DataFrame, data: pd.DataFrame):
    click.echo("ingesting vector data into vector databases")
    if not data.empty and not metadata.empty:
        vectorizer.loadData(data,metadata)
        click.echo("Schema ingestion complete")
    else:
        click.echo("No metadata found to ingest")
def run_pipeline(self,config_file):
    click.echo(f"Reading config from {config_file}")
    with open(config_file, 'r') as f:
        config = json.load(f)
    trino_retriever = get_retriver(config)
    
    vector_store = vector_store(config)

    for catalog in config['catalogs']:
        metadata_df = discover_schema(trino_retriever, catalog)
        ingestData(vector_store,metadata_df)

            
if __name__ == '__main__':
    run_pipeline()