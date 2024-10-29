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

# Evapine Integration Progress Report - October 29, 2024

### Overview
The **Evapine** project integrates a Custom GPT instance (Eva) with Pinecone's Assistant for retrieval-augmented generation (RAG). Below is a detailed progress report on what we have achieved so far.

### Completed Steps

1. **Project Initialization**
   - Created a new GitHub repository: [evapine](https://github.com/safarivis/evapine).
   - Set up the repository with necessary files, including `README.md`, integration scripts, and environment configurations (`fly.toml`).

2. **AI Assistant Development**
   - Created a custom AI assistant called **Evapine** using OpenAI's GPT, integrated with Pinecone for enhanced data retrieval.
   - Evapine allows accurate and context-rich responses by utilizing retrieval-augmented generation.

3. **Hosting and Deployment**
   - Deployed **Evapine** to **Fly.io** for cloud hosting.
   - Utilized Fly.io as the platform to host our application, giving it an accessible link: [https://evapine.fly.dev](https://evapine.fly.dev).
   - Configured Fly.io with necessary environment variables, including `OPENAI_API_KEY` and `PINECONE_API_KEY`, using Fly.io's secure secrets storage.

4. **Infrastructure Setup**
   - Configured the application infrastructure to run as a "machine" in Fly.io, enabling access over the web.
   - Prepared the `fly.toml` file for setting up app configurations like build settings, runtime, and environment variables.
   - Deployment completed successfully; application is live.

### Challenges and Mitigations
- **Buildpack Detection Issues**: Initial deployment faced buildpack-related errors, particularly when using **Heroku Buildpacks**. To mitigate this, we created a `Dockerfile` to specify the build environment explicitly.
- **Secrets Handling**: Fly.io flagged some environment variables as potentially sensitive. We resolved this by using Fly.io's secure secret storage.
- **Database Integration Pending**: Currently, the application is not linked to a database for persistent data storage. A **PostgreSQL** database setup with **Supabase** is planned to store user interactions and enrich the assistant's learning capabilities.

### Next Steps
1. **Database Integration**
   - Link Evapine to a PostgreSQL database (e.g., Supabase) for data storage and retrieval.
   - Update the application code to ensure seamless saving and retrieval of data from the database.

2. **Application Testing**
   - Test Evapine for functionality and robustness via the link: [https://evapine.fly.dev](https://evapine.fly.dev).
   - Address any issues found during testing, specifically related to data saving and API responses.

3. **IP Address Assignment**
   - Evaluate the need for a dedicated IP address to facilitate custom domain routing or direct access.

4. **Documentation Update**
   - Enhance documentation to include detailed deployment instructions, environment configuration, and troubleshooting guides.

### Conclusion
The Evapine project is live and successfully deployed to Fly.io. We have set up the core AI assistant features and made it accessible through a public link. The next phase will focus on data persistence by integrating a PostgreSQL database to allow the assistant to remember user interactions and improve its responses.

We welcome any contributions or suggestions. Please open an issue or pull request in the [GitHub repository](https://github.com/safarivis/evapine) if you have ideas for improvement.

**Contact**: For questions, please contact the project owner at [louisrdup@gmail.com](mailto:louisrdup@gmail.com).

---

### Release Notes - October 29, 2024

**Version 1.0 - Initial Release**

**Key Features**
- Integration of a Custom GPT (Eva) with Pinecone's Assistant to enhance data retrieval.
- Deployment to Fly.io, making the application accessible through a public link.
- Set up infrastructure for scalable cloud hosting using Fly.io machines.

**Known Issues**
- No current database integration: persistent data storage not yet implemented.
- Buildpack-related issues initially encountered; mitigated by using a Dockerfile.

**Next Steps**
- Database setup and integration (Supabase/PostgreSQL).
- Testing and resolving any discovered issues during application usage.

Feel free to contribute or suggest improvements via the [GitHub repository](https://github.com/safarivis/evapine).

**Contact**: [louisrdup@gmail.com](mailto:louisrdup@gmail.com)

