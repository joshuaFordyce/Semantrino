import os

import trino

class trinoConnect:

    def __init__(self,host, port, user,catalog,schema):
        self.trino_host = host
        self.trino_port = port
        self.trino_user = user
        self.catalog = catalog
        self.schema = schema
        

    def configureConnection(self):
        try:
            conn = trino.dbapi.connect(
                host=self.trino_host,
                port=self.trino_port,
                user=self.trino_user,
                catalog=self.catalog,
                schema=self.schema,

                )

            conn.cursor()
            return conn.cursor()
        except trino.dbapi.DatabaseError as e:
            print(f"error:{e}")
        finally:
            pass
        
    


    def mainQuery(self,Query):
        try:
            cur = self.configureConnection()
            cur.execute(Query)
            rows = cur.fetchall
            mainQuerymetrics = cur.stats
            return [rows,cur.description]
        except trino.dbapi.DatabaseError as e:
            print(f"This is the error {e}")
        
        finally:
            if 'cur' in locals() and cur:
                cur.close()
            

    def RagQuery(self,RagQuery):
        try:
            cur = self.configureConnection()
            cur.execute(f'{RagQuery}.INFORMATION_SCHEMA')
            rows = cur.fetchall()
        
            metadataQuerymetrics = cur.stats
            return rows
        except trino.dbapi.DatabaseError as e:
            print(f"this is the error {e}")
        
        finally:
            if 'cur' in locals() and cur:
                cur.close()