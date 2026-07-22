from utils.llm import explain_concept
from utils.summarizer import summarize_text
from utils.search_engine import search
import streamlit as st

st.set_page_config(
    page_title="ArXiv Research Chatbot",
    layout="wide"
)

st.title("📚 ArXiv Research Chatbot")
st.write("Search Computer Science Research Papers")

query = st.text_input("Enter your research topic")

if st.button("Search"):

    if query:

        papers = search(query)

        for i, paper in enumerate(papers):

            st.subheader(f"Paper {i+1}")

            st.write("### Title")
            st.write(paper["title"])

            st.write("### Categories")
            st.write(paper["categories"])

            st.write("### Abstract")
            st.write(paper["abstract"])

            st.write("### Summary")
            st.success(summarize_text(paper["abstract"]))

            st.write("### AI Explanation")

    if st.button(f"Explain Paper {i+1}", key=f"explain_{i}"):

     with st.spinner("Generating explanation..."):

        explanation = explain_concept(
            f"""
            Paper Title:
            {paper['title']}

            Abstract:
            {paper['abstract']}
            """
        )

        st.info(explanation)