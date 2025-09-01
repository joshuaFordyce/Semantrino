Semantrino: A Trino-Native Semantic Search Connector
The Semantrino project is a Go-based tool that provides a native way to perform semantic search within Trino. It addresses the challenge of a disconnect between structured data in Trino and unstructured data in vector databases by providing a seamless, hybrid search experience. The tool is designed to be a high-performance, low-latency solution that can be used for a wide range of data types.

Key Features
Native Semantic Search: A new Trino connector that provides a native way to perform semantic search, using custom SQL functions (e.g., SEMANTIC_SEARCH()).

Hybrid Search: Allows users to combine semantic search with standard SQL queries, providing a powerful and flexible search experience.

Real-time Embeddings: Provides a way to update vector embeddings in real-time as new data is ingested into Trino.

Multi-Vector Search: Supports multiple vector embedding models for different data types.

Design & Architecture
Problem Statement
The existing data platforms, like Trino, are primarily designed for structured data. There is a disconnect between the two, which makes it difficult for a data scientist to combine semantic search results with traditional SQL queries. The goal is to bridge this gap by providing a native way to perform semantic search in Trino.

Solution Overview
Semantrino is a hybrid solution that combines a Go-based Trino connector with a Python-based AI service. The Go connector is the high-performance, low-latency component that runs natively alongside Trino. It acts as a fast, reliable proxy to the Python service, which handles all the heavy lifting of interacting with LLMs and vector databases.

High-Level Workflow
A user submits a SQL query to Trino that contains a new custom function, SEMANTIC_SEARCH().

Trino's query planner recognizes the custom function and, through its plugin interface, delegates the execution of that function to your Go-based connector.

The Go connector acts as a high-performance proxy. It takes the user's query and sends an API call (e.g., a gRPC or REST request) to the Python-based AI service.

The Python service receives the request, sends a call to the LLM API to generate a vector embedding for the user's query, and then uses that embedding to query the vector database for a set of candidate results.

The Python service returns the vector search results to the Go connector.

The Go connector takes these results and uses them to construct a standard SQL query that it can then execute on Trino to get the full rows of data.

The final result is returned to the user, providing a powerful, hybrid search experience.

Architecture Flow
+----------------+      +-----------------+      +-----------------+      +-----------------+
| User (SQL)     | ---> | Trino Cluster   | ---> | Semantrino Go   | ---> | Semantrino      |
|                |      | (Go Connector)  |      | Connector       |      | Python Service  |
+----------------+      +-----------------+      +-----------------+      +-----------------+
      |                       |                       |                         |
      | (1) Submit Query      | (2) API Call to Go    | (3) gRPC/REST Call      | (4) Interact w/
      | (e.g., SELECT...)     | Connector             | (e.g., /search)         |     LLM & Vector DB
      V                       V                       V                         V
+----------------+      +-----------------+      +-----------------+      +-----------------+
| Vector DB      | <--- | Semantrino      | <--- | Python Service  | <--- | LLM API         |
|                |      | (Data)          |      | (Embeddings)    |      | (Embeddings)    |
+----------------+      +-----------------+      +-----------------+      +-----------------+
Getting Started
Prerequisites
A Trino cluster with JMX enabled.

A vector database (e.g., Pinecone, Milvus) configured.

A Go environment (Go 1.22.2 or newer) and Python 3.8+ for building the services.

Docker for building the container images.

Installation
Clone the Repository:
git clone https://github.com/<your-username>/semantrino.git
cd semantrino

Build and Deploy:
make build
make deploy

Contributing
This is an open-source project, and contributions are highly welcome. To get started:

Fork this repository.

Clone your forked repository to your local machine.

Create a new branch for your feature or bug fix.

Submit a pull request to the main branch with a clear description of your changes.

License
This project is licensed under the Apache 2.0 License.