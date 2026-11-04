import pytest
import allure
from services.auth.post_register_user import RegisterUser
from utils.helpers import Helper
from services.auth.post_login_user import LoginUser


@allure.feature('Auth')
class TestAuth:
    helper = Helper()

    @pytest.mark.regression
    @pytest.mark.smoke
    @allure.title('Регистрация пользователя с валидными данными')
    @allure.testcase("https://jira.example.com/TC-11", "TC-11")
    def test_register_user(self, env_config):
        with allure.step('Регистрация пользователя'):
            response, validated_data = RegisterUser(env_config).register_user(
                email='eve.holt@reqres.in',
                password='qwerty1234',
            )
            self.helper.attach_response(response)
        with allure.step('Проверка статус кода'):
            assert response.status_code == 200
        with allure.step('Проверка полученных данных'):
            assert validated_data.id
            assert validated_data.token

    @pytest.mark.regression
    @allure.title('Регистрация пользователя без пароля')
    @allure.testcase("https://jira.example.com/TC-11", "TC-11")
    def test_register_user_validation(self, env_config):
        with allure.step('Регистрация пользователя без пароля'):
            response, error = RegisterUser(env_config).register_user(
                email='eve.holt@reqres.in',
                password=None,
                validate_resp=False,
                validate_reqst=False,
                errors=True
            )
            self.helper.attach_response(response)
        with allure.step('Проверка статус кода'):
            assert response.status_code == 400
        with allure.step('Проверка ошибки'):
            assert error.error

    @pytest.mark.regression
    @allure.title('Авторизация пользователя с валидными данными')
    @allure.testcase("https://jira.example.com/TC-12", "TC-12")
    def test_login_user(self, env_config):
        with allure.step('Регистрация пользователя'):
            email: str = 'eve.holt@reqres.in'
            password: str = 'qwerty1234'
            response1, validated_data1 = RegisterUser(env_config).register_user(
                email=email,
                password=password,
            )
            self.helper.attach_response(response1)
            token = validated_data1.token
        with allure.step('Проверка статус кода'):
            assert response1.status_code == 200
        with allure.step('Авторизация пользователя'):
            response2, validated_data2 = LoginUser(env_config).login_user(
                email=email,
                password=password
            )
            self.helper.attach_response(response2)
        with allure.step('Проверка статус кода'):
            assert response2.status_code == 200
        with allure.step('Проверка токена'):
            assert validated_data2.token == token

    @pytest.mark.regression
    @allure.title('Авторизация пользователя без пароля')
    @allure.testcase("https://jira.example.com/TC-13", "TC-13")
    def test_login_user_not_password(self, env_config):
        with allure.step('Регистрация пользователя'):
            email: str = 'eve.holt@reqres.in'
            password: str = 'qwerty1234'
            response1, validated_data1 = RegisterUser(env_config).register_user(
                email=email,
                password=password,
            )
            self.helper.attach_response(response1)
        with allure.step('Проверка статус кода'):
            assert response1.status_code == 200
        with allure.step('Авторизация пользователя'):
            response2, error = LoginUser(env_config).login_user(
                email=email,
                password = None,
                validate_resp=False,
                validate_reqst=False,
                errors=True
            )
        with allure.step('Проверка статус кода'):
            assert response2.status_code == 400
        with allure.step('Проверка ошибки'):
            assert error.error

