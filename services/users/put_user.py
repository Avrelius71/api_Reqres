from services.base_api import BaseAPI
from services.users.models.users import UpdateUserResponse


class PutUser(BaseAPI):

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)

    def put_user(self, users_id, name: str, job: str, validate: bool = True):
        """Редактирование пользователя.

        Args:
            name (str): Имя пользователя
            job (str): Должность пользователя
        """
        data = {"name": name, "job": job}
        response = self.session.put(f"{self.base_url}/users/{users_id}", json=data)
        validated = None
        if validate:
            validated = UpdateUserResponse.model_validate(response.json())
        return response, validated

