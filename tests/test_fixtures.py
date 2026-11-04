import pytest
from faker import Faker
import requests


fake = Faker()


@pytest.fixture
def user_data():
    return {"name": fake.name(), "job": fake.job()}


def create_user(data):
    response = requests.post(
        'https://reqres.in/api/users',
        json=data,
        headers={'x-api-key': 'reqres_e44008e18f4a40238956f1f5591a7973'}
    )
    return response


def test_create_user(user_data):
    response = create_user(user_data)
    assert response.status_code == 201
