import chromadb
from config import CHROMA_CONFIG

class VectorDBClient:
    def __init__(self):
        self.client = chromadb.HttpClient(host=CHROMA_CONFIG['host'], port=CHROMA_CONFIG['port'])
        self.collection = self.client.get_or_create_collection(CHROMA_CONFIG['collection'])

    def insert_chunks(self, chunk_texts, metadatas, embeddings):
        # Idempotent bulk upsert of (text, metadata, vector)
        ids = [f"chunk_{i}" for i in range(len(chunk_texts))]
        self.collection.upsert(ids=ids, embeddings=embeddings, documents=chunk_texts, metadatas=metadatas)

    def top_k_search(self, query_vector, k=5):
        # Placeholder for ANN search logic with proper filter support
        pass

    def count_chunks(self):
        return self.collection.count()
