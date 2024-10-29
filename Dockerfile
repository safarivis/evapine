# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variables for Pinecone and OpenAI keys
ENV PINECONE_API_KEY=${PINECONE_API_KEY}
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# Run the application
CMD ["python", "integration.py"]

