import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend import app 


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calculate_square(client):
    """
    Test the /square endpoint for valid input.
    """
    response = client.get('/square?number=4')
    assert response.status_code == 200
    data = response.get_json()
    assert data['square'] == 16

def test_calculate_square_invalid_input(client):
    """
    Test the /square endpoint for invalid input.
    """
    response = client.get('/square?number=abc')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
