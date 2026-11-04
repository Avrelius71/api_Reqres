from services.base_api import BaseAPI
from services.users.models.users import UsersListResponse


class GetUsers(BaseAPI):

    def __init__(self, env_config):
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)

    def get_all_user(self, page):
        """Получение cписка пользователей.

                Args:
                    page (int): номер страницы

                Returns:
                    Dict: Cписок пользоватлей
                """
        response = self.session.get(f'{self.base_url}/users?page={page}')
        validated = UsersListResponse.model_validate(response.json())
        return response, validated
