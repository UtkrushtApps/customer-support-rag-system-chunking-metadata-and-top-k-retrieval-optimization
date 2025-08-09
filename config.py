SUPPORT_DOCS_PATH = "data/support_tickets.csv"  # Pre-placed CSV document
CHUNK_SIZE = 200
CHUNK_OVERLAP = 200

CHROMA_CONFIG = {
    "host": "chromadb",
    "port": 8000,
    "collection": "support_docs"
}
