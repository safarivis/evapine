import os
import psycopg2
from pinecone import Pinecone

# Environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
PINECONE_INDEX_NAME = "books"

# Pinecone setup
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

# PostgreSQL setup
def connect_to_postgres():
    """Function to connect to Postgres database"""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        print("Database connection successful")
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

# Function to add a new namespace in Pinecone
def add_namespace(namespace):
    """Function to create a new namespace within the 'books' index"""
    try:
        # Add a dummy vector to initialize the namespace, since Pinecone does not have an explicit create namespace function.
        # We'll add a dummy entry with a random vector and immediately delete it if needed.
        dummy_vector_id = "dummy_vector"
        dummy_values = [0.0] * 1536  # Assumes vector size of 1536
        index.upsert(vectors=[(dummy_vector_id, dummy_values)], namespace=namespace)
        # Optionally delete the dummy vector if you just want to create the namespace
        index.delete(ids=[dummy_vector_id], namespace=namespace)
        print(f"Namespace '{namespace}' successfully created in the 'books' index.")
    except Exception as e:
        print(f"Failed to add namespace '{namespace}': {e}")

# Function to list all available namespaces in the 'books' index
def list_namespaces():
    """List all available namespaces in the 'books' index"""
    try:
        response = index.describe_index_stats()
        namespaces = response.get('namespaces', {}).keys()
        return list(namespaces)
    except Exception as e:
        print(f"Error listing namespaces: {e}")
        return []

# Function to get relevant data from Pinecone
def get_relevant_data(query, namespace=None):
    """Function to query data from Pinecone"""
    try:
        # Use Pinecone Assistant to retrieve data
        if namespace:
            response = index.query(query=query, namespace=namespace)
        else:
            response = index.query(query=query)
        return response
    except Exception as e:
        print(f"Error retrieving data from Pinecone: {e}")
        return None

# Function to save data to the Postgres database
def save_to_postgres(query, response):
    """Save a query-response pair to the Postgres database"""
    conn = connect_to_postgres()
    if conn:
        try:
            cursor = conn.cursor()
            # Create a table if it does not exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS saved_responses (
                    id SERIAL PRIMARY KEY,
                    query TEXT,
                    response TEXT
                )
            """)
            conn.commit()
            # Insert the data
            cursor.execute("""
                INSERT INTO saved_responses (query, response)
                VALUES (%s, %s)
            """, (query, response))
            conn.commit()
            print("Data saved successfully to Postgres.")
        except Exception as e:
            print(f"Failed to save data to Postgres: {e}")
        finally:
            cursor.close()
            conn.close()

# New Function to set up a namespace table in Postgres
def setup_namespace_table():
    """Set up the namespaces table if it doesn't exist."""
    conn = connect_to_postgres()
    if conn:
        try:
            cursor = conn.cursor()
            # Create the namespaces table if it does not exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS namespaces (
                    id SERIAL PRIMARY KEY,
                    index_name TEXT,
                    namespace TEXT
                )
            """)
            conn.commit()
            print("Namespaces table setup complete.")
        except Exception as e:
            print(f"Error setting up namespaces table: {e}")
        finally:
            cursor.close()
            conn.close()

# New Function to add namespace information to the database
def add_namespace_to_db(index_name, namespace):
    """Add a namespace for a given index to the Postgres database."""
    conn = connect_to_postgres()
    if conn:
        try:
            cursor = conn.cursor()
            # Insert namespace information
            cursor.execute("""
                INSERT INTO namespaces (index_name, namespace) VALUES (%s, %s)
                ON CONFLICT (index_name, namespace) DO NOTHING
            """, (index_name, namespace))
            conn.commit()
            print(f"Namespace '{namespace}' for index '{index_name}' added successfully.")
        except Exception as e:
            print(f"Error adding namespace: {e}")
        finally:
            cursor.close()
            conn.close()

# New Function to get available namespaces for an index
def get_namespaces_for_index(index_name):
    """Retrieve all namespaces available for a specific index from the Postgres database."""
    conn = connect_to_postgres()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT namespace FROM namespaces WHERE index_name = %s
            """, (index_name,))
            namespaces = cursor.fetchall()
            namespace_list = [n[0] for n in namespaces]
            return namespace_list
        except Exception as e:
            print(f"Error retrieving namespaces: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

# New Function to answer namespace-related queries
def query_namespaces(index_name):
    """Function to handle requests for namespace information."""
    namespaces = get_namespaces_for_index(index_name)
    if namespaces:
        return f"The available namespaces for index '{index_name}' are: {', '.join(namespaces)}."
    else:
        return f"No namespaces found for index '{index_name}'. You might want to create new ones!"

# Call this function to set up namespace table on startup
setup_namespace_table()

