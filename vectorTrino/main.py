
import click
import trinoConnect
import pandas as pd
@click.command()
@click.option(
    '--trino-host',
    envvar='Trino_Host',
    default='localhost:8080',
    help='THe host of the trino cluster',
)


def discover_schema(trino_host):
    click.echo("Initializing the CLI and pulling the information schema")
    query = "SHOW tables from Information_schema"
    results = trinoConnect.mainQuery(query)
    columns = [desc[0] for desc in results[1]]
    df = pd.DataFrame.from_records(results[0],columns)
    print(df)
    
    
    
def ingestMetadata():
    click.echo("ingesting metadata from Trino to vectorize")

def ingestData():
    click.echo("ingesting data from Trino")
    

if __name__ == '__main__':
    discover_schema()