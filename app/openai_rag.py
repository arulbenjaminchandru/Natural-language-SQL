import openai
from app.vector_store import search_qdrant
from app.config import config

openai.api_key = config['openai']['api_key']

def get_embedding(text, model="text-embedding-ada-002"):
    response = openai.Embedding.create(input=[text], model=model)
    return response['data'][0]['embedding']

def generate_sql_with_rag(user_query):
    # Get query embedding
    query_embedding = get_embedding(user_query)

    # Retrieve relevant contexts
    contexts = search_qdrant(query_embedding)

    # Combine user query with contexts
    augmented_query = f"Context: {' '.join(contexts)}\nQuery: {user_query}\nGenerate a SQL query for the given context and query."

    # Generate SQL using GPT-4 or GPT-3.5
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a SQL expert. Generate SQL queries based on the given context and user query."},
            {"role": "user", "content": augmented_query}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    sql_query = response['choices'][0]['message']['content'].strip()
    return sql_query
