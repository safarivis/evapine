from pinecone import Pinecone

def get_relevant_data(query):
    try:
        # Replace this with your actual Pinecone API key
        api_key = "<YOUR_PINECONE_API_KEY>"
        pc = Pinecone(api_key=api_key)
        
        # Use evapine to retrieve data
        assistant = pc.assistant.get_assistant(assistant_name="evapine")
        response = assistant.query(query=query)
        return response
    except Exception as e:
        return f"Error retrieving data: {e}"

