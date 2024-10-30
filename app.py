from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Route for home page - Health check
@app.route('/')
def home():
    return "Evapine server is up and running!"

# Route for querying namespace information
@app.route('/namespaces', methods=['GET'])
def get_namespaces():
    index_name = request.args.get('index', 'books')  # Get the index name from query params, default to "books"
    namespaces = query_namespaces(index_name)
    return jsonify({"namespaces": namespaces})

# Start the Flask server
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Use the PORT set in environment variables, default to 8080
    app.run(host='0.0.0.0', port=port)

