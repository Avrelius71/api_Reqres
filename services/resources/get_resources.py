from services.base_api import BaseAPI
from services.resources.models.resource import ResourcesListResponse


class GetResources(BaseAPI):

    def __init__(self, env_config):
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)

    def get_resources(self, validate: bool = True):
        """Получение ресурса по ID.



        Returns:
            List: Данные списка ресурсов
        """
        response = self.session.get(f"{self.base_url}/unknown")
        validated = None
        if validate:
            validated = ResourcesListResponse.model_validate(response.json())
        return response, validated
