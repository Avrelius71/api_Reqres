from services.users.delete_user import DeleteUser


def test_delete_users(env_config):
    response = DeleteUser(env_config).delete_user(2)

    assert response.status_code == 204