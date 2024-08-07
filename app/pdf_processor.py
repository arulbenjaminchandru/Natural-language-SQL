import PyPDF2
import openai
from app.vector_store import add_to_qdrant
from app.config import config

openai.api_key = config['openai']['api_key']

def process_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    # Split text into chunks (you may need to implement a more sophisticated chunking method)
    chunks = text.split('\n\n')

    # Create embeddings
    embeddings = [get_embedding(chunk) for chunk in chunks]

    # Add to Qdrant
    add_to_qdrant(chunks, embeddings)

def get_embedding(text, model="text-embedding-ada-002"):
    response = openai.Embedding.create(input=[text], model=model)
    return response['data'][0]['embedding']

if __name__ == "__main__":
    process_pdf('data/table_descriptions.pdf')
