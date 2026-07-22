from ingest import create_embedding, split_text
from sources.web_sources import fetch_page
import chromadb

client = chromadb.PersistentClient(
    path="./vector_store"
)

collection = client.get_or_create_collection(
    name="knowledge_base"
)

urls = [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Neural_network"
]

for url in urls:
    print(f"Fetching {url}")

    text = fetch_page(url)

    chunks = split_text(text)

    print(f"Created {len(chunks)} chunks")

for idx, chunk in enumerate(chunks):

    embedding = create_embedding(chunk)

    collection.add(
        ids=[f"wiki_{idx}"],
        embeddings=[embedding],
        documents=[chunk]
    )

print("Knowledge stored successfully!")