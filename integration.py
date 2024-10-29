import os
import psycopg2
from pinecone import Pinecone

# Environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

# Pinecone setup
pc = Pinecone(api_key=PINECONE_API_KEY)

# PostgreSQL setup
try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    print("Database connection successful")
except Exception as e:
    print(f"Database connection failed: {e}")

# Function to get relevant data from Pinecone Assistant
def get_relevant_data(query):
    try:
        # Use Pinecone Assistant to retrieve data
        assistant = pc.assistant.get_assistant(assistant_name="evapine")
        response = assistant.query(query=query)
        
        # Save query-response pair to the database
        save_query_response(query, response)
        
        return response
    except Exception as e:
        return f"Error retrieving data: {e}"

# Function to save the query-response pair to the database
def save_query_response(query, response):
    try:
        # SQL query to insert the query-response pair
        insert_query = """
        INSERT INTO interactions (query, response, created_at)
        VALUES (%s, %s, NOW())
        """
        cursor.execute(insert_query, (query, response))
        conn.commit()
        print("Query-response pair saved successfully")
    except Exception as e:
        print(f"Error saving query-response pair: {e}")

# Function to retrieve a response based on a query from the database
def get_response_by_query(query):
    try:
        # SQL query to retrieve response based on the given query
        select_query = """
        SELECT response FROM interactions
        WHERE query = %s
        ORDER BY created_at DESC
        LIMIT 1
        """
        cursor.execute(select_query, (query,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return "No response found for the given query"
    except Exception as e:
        return f"Error retrieving response: {e}"

# Example usage
if __name__ == "__main__":
    test_query = "What's the weather today?"
    
    # Get relevant data using Pinecone Assistant and save to database
    response = get_relevant_data(test_query)
    print("Response from Pinecone Assistant:", response)
    
    # Retrieve the saved response from the database
    retrieved_response = get_response_by_query(test_query)
    print("Retrieved response from database:", retrieved_response)

