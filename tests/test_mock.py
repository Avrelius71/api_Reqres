import pytest
from unittest.mock import patch, Mock
import requests


def process_user_data(user_id: int):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    return {"error": "User not found"}


@patch("requests.get")
def test_data_mock_200(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}

    mock_get.return_value = mock_response

    result = process_user_data(1)

    assert result == {"id": 1, "name": "John Doe"}


@patch("requests.get")
def test_data_mock_400(mock_get):

    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    result = process_user_data(999)

    assert result == {"error": "User not found"}