import pytest
from services.users.post_create import CreateUser
from config.environments import Environment, environments, EnvironmentConfig


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="stage",
        help="Окружение для запуска тестов (dev/stage)"
    )


@pytest.fixture(scope="session")
def env(request) -> Environment:
    """Фикстура для получения текущего окружения"""
    env_name = request.config.getoption("--env")
    try:
        return Environment(env_name.lower())
    except ValueError:
        raise ValueError(
            f"Некорректное окружение: {env_name}. "
            f"Используйте одно из: dev/stage/prod"
        )


@pytest.fixture(scope="session")
def env_config(env) -> EnvironmentConfig:
    """Фикстура для получения конфигурации текущего окружения"""
    print(f"\nОкружение: {env}")
    print(f"{environments[env]}\n")
    return environments[env]


@pytest.fixture(scope="session")
def users_id(env_config):
    response, validated = CreateUser(env_config).create_user(
        name="test_qa",
        job="test_qa",
    )
    yield validated.id