from app.openai_rag import generate_sql_with_rag
from app.sql_executor import execute_sql_query

def generate_and_execute_sql(prompt):
    """
    Generate SQL from the given prompt and execute it.
    """
    sql_query = generate_sql_with_rag(prompt)
    result = execute_sql_query(sql_query)
    return {
        "generated_sql": sql_query,
        "execution_result": result["sql_result"],
        "natural_language_response": result["natural_language_response"]
    }
