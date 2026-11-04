from services.base_api import BaseAPI
from services.users.models.users import SingleUserResponse


class GetUser(BaseAPI):

    def __init__(self, env_config):
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)

    def get_user(self, user_id, validate: bool = True):
        """Получение пользователя по ID.

        Args:
            user_id (int): ID пользователя

        Returns:
            Dict: Данные пользователя
        """
        response = self.session.get(f"{self.base_url}/users/{user_id}")
        validated = None
        if validate:
            validated = SingleUserResponse.model_validate(response.json())
        return response, validated
