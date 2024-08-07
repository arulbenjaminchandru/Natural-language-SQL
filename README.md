# Natural Language to SQL Query Generator

This project allows users to input natural language queries, which are then converted to SQL and executed on a PostgreSQL database containing healthcare claims data.

## Setup

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your configuration in `config.yaml`
4. Create the database tables and insert sample data using `data/sample_data.sql`
5. Process the table descriptions: `python -m app.pdf_processor`
6. Start the FastAPI server: `uvicorn app.main:app --reload`

## Usage

Send a POST request to the `/generate_and_execute_sql/` endpoint with a JSON body containing a `user_message`. For example:

```json
{
  "user_message": "Show me all claims for patient John Doe"
}