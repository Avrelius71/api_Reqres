from services.users.get_user import GetUser
import pytest


@pytest.mark.parametrize('user_id', [1, 2, 3])
def test_get_users(env_config, user_id):
    response, validated_data = GetUser(env_config).get_user(user_id)

    assert response.status_code == 200
    assert validated_data.data.id == user_id
