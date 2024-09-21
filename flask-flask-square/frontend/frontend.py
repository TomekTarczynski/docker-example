import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Fetch the backend URL from the environment
backend_url = os.getenv('BACKEND_URL', 'http://localhost:3001')

@app.route('/')
def index():
    """
    Render the main webpage.
    """
    return render_template('index.html')

@app.route('/proxy_square', methods=['GET'])
def proxy_square():
    """
    Proxy request to the backend to calculate the square of a number.
    
    Expects a 'number' as a query parameter and makes a request to the backend API.
    """
    number = request.args.get('number')
    if not number:
        return jsonify({'error': 'Please provide a number.'}), 400

    # Make a request from the frontend (Python) to the backend API
    try:
        backend_response = requests.get(f'{backend_url}/square', params={'number': number})
        backend_response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return backend_response.json()  # Return the backend API response to the browser
    except requests.RequestException as e:
        return jsonify({'error': f'Error while connecting to the backend: {str(e)}'}), 500

if __name__ == '__main__':
    frontend_port = os.getenv('FRONTEND_PORT', 3000)
    app.run(debug=True, host='0.0.0.0', port=frontend_port)
