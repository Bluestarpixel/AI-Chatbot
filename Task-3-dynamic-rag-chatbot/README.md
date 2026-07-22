# Dynamic Knowledge Base Chatbot

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) style chatbot with a dynamically expandable knowledge base. The chatbot collects information from external sources, converts the content into vector embeddings, stores them in a vector database, and retrieves relevant information based on user queries.

The system also includes an automatic update mechanism that periodically checks data sources for changes and updates the knowledge base accordingly.

---

## Features

* Website content ingestion
* Text chunking and preprocessing
* Semantic embeddings using Sentence Transformers
* Vector storage using ChromaDB
* Semantic similarity search
* Interactive chatbot interface
* Automatic scheduled updates using APScheduler
* Content change detection using SHA-256 hashing
* Extensible architecture for multiple knowledge sources

---

## Technologies Used

### Programming Language

* Python 3.14

### Libraries

* Sentence Transformers
* ChromaDB
* APScheduler
* Requests
* BeautifulSoup4
* Hashlib

### Storage

* ChromaDB Vector Database

---

## Project Structure

```text
dynamic-rag-chatbot/
│
├── main.py
├── load_data.py
├── update.py
├── retrieve.py
├── ingest.py
├── config.py
├── .env
│
├── sources/
│   └── web_sources.py
│
├── vector_store/
│
└── venv/
```

---

## System Workflow

### Knowledge Ingestion

1. Fetch content from a website.
2. Extract text using BeautifulSoup.
3. Split content into chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in ChromaDB.

### User Query Flow

1. User enters a question.
2. Question is converted into an embedding.
3. ChromaDB performs semantic similarity search.
4. Most relevant chunks are retrieved.
5. Results are displayed to the user.

### Automatic Update Process

1. APScheduler triggers periodic checks.
2. Website content is downloaded.
3. SHA-256 hash is generated.
4. Hash is compared with the previous version.
5. If content changes:

   * New content is processed.
   * New embeddings are generated.
   * Vector database is updated.

---

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install chromadb
pip install sentence-transformers
pip install apscheduler
pip install beautifulsoup4
pip install requests
```

---

## Running the Project

### Load Knowledge

```bash
python load_data.py
```

### Start Chatbot

```bash
python main.py
```

### Run Automatic Updater

```bash
python update.py
```

---

## Example Query

```text
Ask a question:
What is Artificial Intelligence?
```

Example Output:

```text
Artificial Intelligence is the ability of machines to perform tasks that typically require human intelligence such as learning, reasoning, and problem solving.
```

---

## Future Enhancements

* Support for PDF ingestion
* GitHub repository indexing
* Notion and Confluence integration
* Multi-source knowledge aggregation
* LLM-generated answers using retrieved context
* Real-time updates using webhooks
* Metadata filtering and ranking
* User authentication and chat history

---

## Conclusion

This project demonstrates a complete pipeline for building a dynamic knowledge-based chatbot. The system can continuously expand and refresh its knowledge base by monitoring external information sources and updating the vector database automatically.
