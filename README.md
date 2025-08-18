Semantrino
Introduction: The Semantrino project is a Go-based tool that extends Trino's functionality by providing a native way to perform semantic search. By integrating a vector database and an API for generating vector embeddings, this tool simplifies the process of combining semantic search with traditional SQL queries.
Features:
Native Semantic Search: A new Trino connector that provides a native way to perform semantic search.
Hybrid Search: Allow users to combine semantic search with standard SQL queries.
Real-time Embeddings: Provide a way to update vector embeddings in real-time as new data is ingested into Trino.
Key Differentiators:
Native, Go-based Connector: The primary differentiator is that Semantrino is a Go-based Trino connector. It's a high-performance, low-latency solution that runs directly inside the Trino process.
Hybrid Search: The tool's ability to combine semantic search with traditional SQL queries is a key differentiator.
Real-time Embeddings: The tool's ability to update vector embeddings in real-time is a major differentiator.
Getting Started:
Prerequisites: A Trino cluster with JMX enabled, a vector database, and a Go environment.
Installation: git clone ..., make deploy
Usage: semantrino search "my query"