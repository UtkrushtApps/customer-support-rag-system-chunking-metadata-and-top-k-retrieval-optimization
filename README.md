# Task Overview

You are improving a customer support RAG system built on Chroma and FastAPI. Today, the system underdelivers on search result relevance due to poor document chunking and missing metadata, causing retrieval quality and user experience issues.

- The document ingestion, embedding, and API layers are fully automated. You only need to improve the retrieval logic, chunking, and metadata enrichment within the existing pipeline.
- Current issues include large, non-overlapping text chunks (2000 tokens) that blur support topics, and missing support metadata such as category, priority, and date.
- The vector database contains all embeddings already; you will re-process them for optimized chunking, attach metadata, and configure ANN retrieval to boost recall and efficiency.
- Your work will enable users to receive the top-5 most contextually relevant support passages for any query, measured using both manual spot checks and recall@k evaluation scripts.

## What Needs Improvement
- Inefficient chunking: chunks are too big, not overlapping, and contextually imprecise.
- Metadata missing: users can't filter or rank by category, priority, or recency.
- ANN search and retrieval poorly configured: Chroma defaults need tuning for this data and embedding model.
- Retrieval logic: returns many irrelevant or distant matches.

## Database Access
- **Vector database:** Chroma (host: `<DROPLET_IP>`, port: 8001, collection: `support_docs`)
- **Embedding dimension:** 384 (sentence-transformers)
- **Chunk metadata fields:** `category` (string), `priority` (int), `date` (ISO string), plus internal Chroma IDs
- **Collection size:** 8,000+ support documents, chunked into several thousand records
- You may use Chroma's Python client to inspect collections and verify inserts/retrievals.

## Objectives
- Implement overlapping chunking (target: 200 tokens per chunk, 200-token overlap)
- Each retrieved chunk must include metadata: category, priority, date
- Optimize Chroma collection/vector search settings for effective ANN retrieval using cosine similarity
- Implement a top-5 similarity search that returns the most contextually accurate support answers
- Provide evidence of improved recall@5 with provided queries

## How to Verify
- Use the FastAPI `/search` endpoint with sample queries from `sample_queries.txt`
- Examine returned passages for accuracy, coverage, and metadata completeness
- Run provided evaluation script to measure recall@5 and inspect improvement vs baseline
- Manual spot check for topic coverage and relevance sufficiency
