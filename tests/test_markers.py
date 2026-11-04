import pytest
import requests
import os
from faker import Faker


headers = {'x-api-key': 'reqres_e44008e18f4a40238956f1f5591a7973'}
fake = Faker()


@pytest.mark.regression
@pytest.mark.smoke
def test_get_user_list():
    response = requests.get(
        url='https://reqres.in/api/users',
        headers=headers
    )
    assert response.status_code == 200


@pytest.mark.regression
@pytest.mark.smoke
def test_create_user():
    data = {'name': fake.name(), 'job': fake.job()}
    response = requests.post(
        'https://reqres.in/api/users',
        json=data,
        headers=headers
    )
    assert response.status_code == 201


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.skipif(not os.getenv("ENABLE_UPDATE_TEST"),
    reason="Тест пропускается: переменная окружения ENABLE_UPDATE_TEST не установлена")
def test_update_user():
    data = {'name': fake.name(), 'job': fake.job()}
    response = requests.put(
        'https://reqres.in/api/users/2',
        json = data,
        headers=headers
    )
    assert response.status_code == 200
