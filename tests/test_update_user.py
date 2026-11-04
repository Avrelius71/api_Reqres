from services.users.patch_user import PatchUser

data = {'name': 'Artem', 'job': 'Legendary AQA'}


def test_update_user(env_config, users_id):
    response, validated = PatchUser(env_config).patch_user(
        users_id,
        name='Artem',
        job='Legendary AQA'
    )

    assert response.status_code == 200
    assert validated.name == "Artem"
    assert validated.job == "Legendary AQA"
    assert validated.updatedAt is not None