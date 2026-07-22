import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading Computer Science papers...")

# Load only the first 10,000 papers
df = pd.read_csv("data/cs_papers.csv", nrows=10000)

# Remove missing values
df = df.dropna()

# Combine title and abstract
documents = df["title"] + " " + df["abstract"]

vectorizer = TfidfVectorizer(stop_words="english")

vectors = vectorizer.fit_transform(documents)

print("Search Engine Ready!")

def search(query, top_k=5):

    query_vector = vectorizer.transform([query])

    similarity = cosine_similarity(query_vector, vectors)

    indices = similarity.argsort()[0][-top_k:][::-1]

    results = []

    for idx in indices:

        results.append({
            "title": df.iloc[idx]["title"],
            "abstract": df.iloc[idx]["abstract"],
            "categories": df.iloc[idx]["categories"]
        })

    return results