# Evapine: Custom GPT Integration with Pinecone Assistant

## Overview
Evapine is a project that integrates a Custom GPT instance (Eva) with Pinecone's Assistant for seamless retrieval-augmented generation (RAG). The main goal is to create a user interface through Custom GPT (Eva) while using Pinecone to manage the data retrieval and augment Eva's responses with relevant, specific data.

This repository includes scripts and configuration files needed to set up the Pinecone Assistant and integrate it into Custom GPT Eva, allowing efficient retrieval of user documents and providing enriched responses.

## Features
- **Custom GPT User Interface**: Eva serves as the Custom GPT interface, handling user queries.
- **Pinecone Assistant Integration**: Utilizes Pinecone's Assistant to manage document embeddings, providing accurate and contextually relevant responses.
- **Retrieval-Augmented Generation (RAG)**: Evapine augments Eva's capabilities to answer questions using user-provided documents, reducing hallucinations and increasing accuracy.

## Prerequisites
To get started, you'll need:
- **Python 3.10 or later**
- **Pinecone API Key**
- **OpenAI API Key**
- **Poetry** for dependency management
- **Git** for managing the repository

## Setup Instructions

### 1. Clone the Repository
Clone the repository from GitHub to your local machine:

```bash
$ git clone https://github.com/safarivis/evapine.git
$ cd evapine
```

### 2. Set Up Environment Variables
Add the following environment variables:

- **PINECONE_API_KEY**: Your Pinecone API key.
- **PINECONE_ENVIRONMENT**: Set to your Pinecone environment (e.g., "us-east-1").
- **OPENAI_API_KEY**: Your OpenAI API key for GPT functionality.

Add these to your `.bashrc` or `.env` file for convenience.

### 3. Install Dependencies
Use Poetry to create a virtual environment and install all dependencies:

```bash
$ poetry install
```

### 4. Create the Pinecone Assistant
Run the script to create the Pinecone Assistant instance that Eva will interact with:

```python
from pinecone import Pinecone

api_key = "<YOUR_PINECONE_API_KEY>"
pc = Pinecone(api_key=api_key)

assistant = pc.assistant.create_assistant(
    assistant_name="evapine",
    metadata={"author": "louisrdup@gmail.com", "version": "1.0"},
    timeout=30
)
print("Assistant created successfully:", assistant)
```

### 5. Deploy to Fly.io or Render.com
To make your assistant available, you can deploy this app to a cloud platform:

- **Fly.io**: Connect your GitHub repository and use their UI-based launcher.
- **Render.com**: Similar setup to Fly.io, use GitHub integration for automatic deployment.

## Usage
### Connecting to Custom GPT Eva
1. Add this retrieval plugin as a **Custom Action** to Eva in the OpenAI Custom GPT settings.
2. Import from the URL provided by your Fly.io/Render deployment.
3. Specify actions like retrieving documents or writing responses based on user data.

### Example Function
You can add the following to Eva's function settings to query Pinecone data:

```python
def get_relevant_data(query):
    try:
        assistant = pc.assistant.get_assistant(assistant_name="evapine")
        response = assistant.query(query=query)
        return response
    except Exception as e:
        return f"Error retrieving data: {e}"
```

## Contributing
If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contact
For more information, contact louisrdup@gmail.com.

