from services.users.post_create import CreateUser


def test_create_user(env_config):
    response, validate = CreateUser(env_config).create_user(
        name="John Doe",
        job="QA Engineer"
    )

    assert response.status_code == 201
    assert validate.id is not None
    assert validate.name == "John Doe"
    assert validate.job == "QA Engineer"
