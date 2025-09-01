import os

import trino

class trinoConnection:

    def __init__():
        pass

    def configureConnection(self,paramDict):
        conn = trino.dbapi.connect(
            host='localhost',
            port=8080,
            user='user',
            catalog='tpch',
            schema='the-schema',

        )

        cur = conn.cursor()
        return cur


    def mainQuery(self,Query):
        cur = self.configureConnection()
        cur.execute(Query)
        rows = cur.fetchall
        mainQuerymetrics = cur.stats
        return rows

    def RagQuery(self,RagQuery):
        cur = self.configuremainConnection()
        cur.execute(RagQuery)
        rows = cur.fetchall()
        
        metadataQuerymetrics = cur.stats
        return rows