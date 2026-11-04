from services.base_api import BaseAPI
from services.resources.models.resource import SingleResourceResponse


class GetResource(BaseAPI):

    def __init__(self, env_config):
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)

    def get_resource(self, resource_id, validate: bool = True):
        """Получение ресурса по ID.

        Args:
            resource_id (int): ID ресурса

        Returns:
            Dict: Данные рессурса
        """
        response = self.session.get(f"{self.base_url}/unknown/{resource_id}")
        validated = None
        if validate:
            validated = SingleResourceResponse.model_validate(response.json())
        return response, validated
