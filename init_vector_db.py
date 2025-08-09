import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from config import (SUPPORT_DOCS_PATH, CHUNK_SIZE, CHUNK_OVERLAP, CHROMA_CONFIG)
from db.vector_db_client import VectorDBClient
import numpy as np

def load_support_docs():
    df = pd.read_csv(SUPPORT_DOCS_PATH)
    # Columns: ticket_id, text, category, priority, date
    return df

def chunk_text(text, chunk_size, overlap):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        chunk = ' '.join(words[start:start + chunk_size])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def main():
    print("Loading support documents...")
    df = load_support_docs()
    print(f"{len(df)} docs loaded.")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    chunk_texts, metadatas = [], []
    print("Chunking and attaching metadata...")
    for _, row in df.iterrows():
        chunks = chunk_text(row["text"], CHUNK_SIZE, CHUNK_OVERLAP)
        for idx, chunk in enumerate(chunks):
            chunk_texts.append(chunk)
            metadatas.append({
                "category": row["category"],
                "priority": int(row["priority"]),
                "date": row["date"]
            })
    print(f"{len(chunk_texts)} chunks prepared.")
    print("Generating embeddings...")
    embeddings = model.encode(chunk_texts, batch_size=32, show_progress_bar=True)
    vdb = VectorDBClient()
    vdb.insert_chunks(chunk_texts, metadatas, embeddings)
    print("[Done] All chunks re-processed and indexed.")

if __name__ == "__main__":
    main()
