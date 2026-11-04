from services.base_api import BaseAPI
from services.auth.models.auth import LoginRequest, LoginResponse, ErrorResponse


class LoginUser(BaseAPI):
    def __init__(self, env_config):
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)

    def login_user(self, email: str, password: str, validate_resp=True, validate_reqst=True, errors=False):
        data = {'email': email, 'password': password}
        if validate_reqst:
            request_data = LoginRequest.model_validate(data)
        response = self.session.post(
            f'{self.base_url}/login',
            json=data
        )
        validated = None
        if validate_resp:
            validated = LoginResponse.model_validate(response.json())
            return response, validated
        error = None
        if errors:
            error = ErrorResponse.model_validate(response.json())
            return response, error
