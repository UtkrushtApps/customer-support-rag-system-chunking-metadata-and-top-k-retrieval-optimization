#!/bin/bash
set -e

echo "[1/3] Launching Chroma vector store and FastAPI..."
docker-compose up -d
sleep 12

echo "[2/3] Running document ingestion/chunking and embedding..."
docker exec supportapi python init_vector_db.py

echo "[3/3] Verifying Chroma index and search readiness..."
docker exec supportapi python -c "import db.vector_db_client as vdb; assert vdb.count_chunks() > 0, 'No chunks indexed'"
echo "[OK] Setup complete. Ready for retrieval logic testing."
