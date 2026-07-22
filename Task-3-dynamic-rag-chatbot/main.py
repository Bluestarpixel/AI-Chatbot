from ingest import create_embedding
from retrieve import search

while True:
    question = input("\nAsk a question (or type quit): ")

    if question.lower() == "quit":
        break

    query_embedding = create_embedding(question)

    results = search(query_embedding)

    print("\nTop Match:\n")

    try:
        print(results["documents"][0][0])
    except:
        print("No results found.")