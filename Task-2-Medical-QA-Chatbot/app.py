import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from medical_ner import extract_entities


@st.cache_resource
def load_data():
    df = pd.read_csv("medical_qa.csv")
    df = df.dropna(subset=["question", "answer"])

    vectorizer = TfidfVectorizer(stop_words="english")
    question_vectors = vectorizer.fit_transform(df["question"])

    return df, vectorizer, question_vectors

df, vectorizer, question_vectors = load_data()

st.title("🏥 Medical Q&A Chatbot")

user_query = st.text_input("Ask a medical question")

if st.button("Submit"):

    entities = extract_entities(user_query)

    st.subheader("Detected Medical Terms")
    st.write(entities)

    query_vector = vectorizer.transform([user_query])

    similarities = cosine_similarity(
        query_vector,
        question_vectors
    )

    best_match = similarities.argmax()

    st.subheader("Answer")
    st.write(df.iloc[best_match]["answer"])