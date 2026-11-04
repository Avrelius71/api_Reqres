from services.base_api import BaseAPI
from services.users.models.users import UpdateUserRequest, UpdateUserResponse


class PatchUser(BaseAPI):

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)

    def patch_user(
            self,
            users_id: int,
            job: str = None,
            name: str = None,
            validate: bool = True,
            validate_request: bool = True
    ):
        """Редактирование пользователя.

        Args:
            name (str): Имя пользователя
            job (str): Должность пользователя
        """
        data = {}
        if name is not None:
            data['name'] = name
        if job is not None:
            data['job'] = job
        if validate_request:
            UpdateUserRequest.model_validate(data)
        response = self.session.patch(f"{self.base_url}/users/{users_id}", json=data)
        validated = None
        if validate:
            validated = UpdateUserResponse.model_validate(response.json())
        return response, validated
