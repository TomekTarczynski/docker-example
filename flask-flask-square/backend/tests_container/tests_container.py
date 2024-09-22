import requests

def test_square_endpoint():
    """
    Test the /square endpoint.
    """
    response = requests.get('http://localhost:3001/square?number=4')
    assert response.status_code == 200
    assert response.json()['square'] == 16

def test_invalid_input():
    """
    Test the /square endpoint with invalid input.
    """
    response = requests.get('http://localhost:3001/square?number=invalid')
    assert response.status_code == 400
    assert response.json()['error'] == 'Invalid input. Please provide a valid number.'
