import psycopg2
from psycopg2.extras import RealDictCursor
from app.config import config
import openai

openai.api_key = config['openai']['api_key']

def execute_sql_query(sql_query):
    """
    Execute the given SQL query and return the results.
    """
    try:
        connection = psycopg2.connect(**config["postgres"])
        
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sql_query)
            
            if cursor.description:  # Check if the query returns any rows
                result = cursor.fetchall()
                natural_language_response = generate_natural_language_response(result)
            else:
                result = f"Query executed successfully. Rows affected: {cursor.rowcount}"
                natural_language_response = "The query was executed successfully, but it did not return any rows."

        connection.commit()
        return {
            "sql_result": result,
            "natural_language_response": natural_language_response
        }

    except psycopg2.Error as e:
        return f"An error occurred: {e}"

    finally:
        if connection:
            connection.close()

def generate_natural_language_response(result):
    """
    Generate a natural language response from the SQL query result.
    """
    # Format the result into a string that can be fed into the OpenAI model
    formatted_result = str(result)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a data analyst. Summarize the SQL query results in natural language."},
            {"role": "user", "content": f"Here are the SQL query results: {formatted_result}"}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    natural_language_summary = response['choices'][0]['message']['content'].strip()
    return natural_language_summary
