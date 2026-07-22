import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading dataset...")

df = pd.read_csv("medical_qa.csv")

df = df.dropna(subset=["question", "answer"])

vectorizer = TfidfVectorizer(stop_words="english")

question_vectors = vectorizer.fit_transform(df["question"])

print("Chatbot Ready!")

while True:

    user_query = input("\nAsk a medical question (or type exit): ")


    if user_query.lower() == "exit":
        break

    query_vector = vectorizer.transform([user_query])

    similarities = cosine_similarity(
        query_vector,
        question_vectors
    )


    best_match = similarities.argmax()


matched_question = df.iloc[best_match]["question"]
answer = df.iloc[best_match]["answer"]

print("\nMatched Question:")
print(matched_question)

print("\nAnswer:")
print(answer)