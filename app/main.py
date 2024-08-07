from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.sql_generator import generate_and_execute_sql

app = FastAPI()

class QueryRequest(BaseModel):
    user_message: str

@app.post("/generate_and_execute_sql/")
async def generate_and_execute_sql_endpoint(query_request: QueryRequest):
    user_message = query_request.user_message

    if not user_message:
        raise HTTPException(status_code=400, detail="Please enter a question.")

    result = generate_and_execute_sql(user_message)
    return result