from sentence_transformers import SentenceTransformer
from config import MODEL_NAME

model = SentenceTransformer(MODEL_NAME)

def create_embedding(text):
    return model.encode(text).tolist()


def split_text(text, chunk_size=500):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks