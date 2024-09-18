from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/square', methods=['GET'])
def calculate_square():
    """
    Calculate the square of a given number.
    
    Expects a number to be passed as a query parameter in the URL.
    Example: /square?number=4 will return 16.

    Returns:
        JSON response containing the original number and its square.
    """
    try:
        # Get the 'number' from the query parameters
        number = float(request.args.get('number'))
        # Calculate the square of the number
        square = number ** 2
        # Return the result as a JSON response
        return jsonify({
            'number': number,
            'square': square
        })
    except (TypeError, ValueError):
        # Handle the case when the query parameter is not a valid number
        return jsonify({
            'error': 'Invalid input. Please provide a valid number.'
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Bind to 0.0.0.0 to allow external access
