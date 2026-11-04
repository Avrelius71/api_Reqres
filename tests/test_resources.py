import pytest
import allure
from services.resources.get_resource import GetResource
from utils.helpers import Helper
from services.resources.get_resources import GetResources


@allure.feature('Resources')
class TestResources:
    helper = Helper()

    @pytest.mark.regression
    @allure.title('Получение одного ресурса')
    @allure.testcase("https://jira.example.com/TC-8", "TC-8")
    def test_get_resources(self, env_config):
        resource_id = 2
        with allure.step('Получаем информацию по ресурсу'):
            response, validated_data = GetResource(env_config).get_resource(resource_id)
            self.helper.attach_response(response)
        with allure.step('Проверяем статус код'):
            assert response.status_code == 200
        with allure.step('Проверяем данные списка'):
            assert validated_data.data.id == resource_id
            assert validated_data.data.name
            assert validated_data.support.text

    @pytest.mark.regression
    @allure.title('Получение несуществующего ресурса')
    @allure.testcase("https://jira.example.com/TC-9", "TC-9")
    def test_not_existent_resource(self,env_config):
        resource_id = 23
        with allure.step('Получаем информацию по несуществующему ресурсу'):
            response, validate_data = GetResource(env_config).get_resource(resource_id, validate=False)
            self.helper.attach_response(response)
        with allure.step('проверка статус кода'):
            assert  response.status_code == 404

    @pytest.mark.regression
    @allure.title('Получение списка ресурсов')
    @allure.testcase("https://jira.example.com/TC-10", "TC-10")
    def test_get_list_resources(self, env_config):
        with allure.step('Получение списка ресурсов'):
            response, validated_data = GetResources(env_config).get_resources()
            self.helper.attach_response(response)
        with allure.step('Проверка статус кода'):
            assert response.status_code == 200
        with allure.step('Проверка получаеммых данных'):
            assert validated_data.data
            assert validated_data.page
            assert validated_data.per_page
            assert validated_data.total
            assert validated_data.total_pages
