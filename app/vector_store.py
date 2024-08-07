from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from app.config import config

client = QdrantClient(url=config['qdrant']['url'], api_key=config['qdrant']['api_key'])

def add_to_qdrant(texts, embeddings):
    client.recreate_collection(
        collection_name="table_descriptions",
        vectors_config=VectorParams(size=len(embeddings[0]), distance=Distance.COSINE),
    )

    client.upload_collection(
        collection_name="table_descriptions",
        vectors=embeddings,
        payload=[{"text": text} for text in texts],
    )

def search_qdrant(query_vector, limit=5):
    results = client.search(
        collection_name="table_descriptions",
        query_vector=query_vector,
        limit=limit
    )
    return [hit.payload['text'] for hit in results]