from services.base_api import BaseAPI
from services.auth.models.auth import RegisterRequest, RegisterResponse, ErrorResponse


class RegisterUser(BaseAPI):

    def __init__(self, env_config):
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)

    def register_user(self, email: str, password: str, validate_resp=True, validate_reqst=True, errors=False):
        data = {'email': email, 'password': password}
        if validate_reqst:
            request_data = RegisterRequest.model_validate(data)
        response = self.session.post(
            f'{self.base_url}/register',
        json=data
        )
        validated = None
        if validate_resp:
            validated = RegisterResponse.model_validate(response.json())
            return response, validated
        error = None
        if errors:
            error = ErrorResponse.model_validate(response.json())
            return response, error


