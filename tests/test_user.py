import allure
import pytest
from services.users.post_create import CreateUser, assert_user_created_correctly
from services.users.delete_user import DeleteUser
from utils.helpers import Helper
from services.users.get_user import GetUser
from services.users.get_users import GetUsers
from services.users.put_user import PutUser
from services.users.patch_user import PatchUser


@pytest.fixture
def created_user_ids():
    """Список ID созданных пользователей для cleanup."""
    return []


@pytest.fixture
def cleanup_users(env_config, created_user_ids):
    """Фикстура для удаления тестовых пользователей после теста."""
    yield  # Тест выполняется здесь

    # Cleanup после теста
    for user_id in created_user_ids:
        try:
            DeleteUser(env_config).delete_user(user_id)
        except Exception as e:
            print(f"Ошибка при удалении {user_id}: {e}")


@allure.feature('Users')
class TestUser:
    helper = Helper()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Создание нового пользователя')
    @allure.testcase("https://jira.example.com/TC-1", "TC-1")
    def test_create_user(self, env_config, cleanup_users, created_user_ids):
        with allure.step('Создаём нового пользователя'):
            response, validated_data = CreateUser(env_config).create_user(
                name="John Doe",
                job="QA Engineer"
            )
            self.helper.attach_response(response)

        with allure.step('Проверяем корректность создания'):
            assert_user_created_correctly(
                response, validated_data, "John Doe", "QA Engineer"
            )

        created_user_ids.append(validated_data.id)

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Получение информации о пользователе')
    @allure.testcase("https://jira.example.com/TC-2", "TC-2")
    def test_get_user(self, env_config):
        user_id = 2

        with allure.step('Получаем пользователя по ID'):
            response, validated_data = GetUser(env_config).get_user(user_id)
            self.helper.attach_response(response)

        with allure.step('Проверяем статус код'):
            assert response.status_code == 200

        with allure.step('Проверяем данные пользователя'):
            assert validated_data.data.id == user_id
            assert validated_data.data.email
            assert validated_data.support.url

    @pytest.mark.regression
    @allure.title('Получение списка пользователей')
    @allure.testcase("https://jira.example.com/TC-3", "TC-3")
    def test_get_all_users(self, env_config):
        page = 2
        with allure.step('Получение списка пользователей'):
            response, validated_data = GetUsers(env_config).get_all_user(2)
            self.helper.attach_response(response)

        with allure.step('Проверяем статус код'):
            assert response.status_code == 200

        with allure.step('Проверяем данные списка'):
            assert validated_data.page == page
            assert validated_data.data
            assert validated_data.support

    @pytest.mark.regression
    @allure.title('Получение несуществующего пользователя - 404')
    @allure.testcase("https://jira.example.com/TC-4", "TC-4")
    def test_get_user_not_exist(self, env_config):
        user_id = 23

        with allure.step('Получаем пользователя по ID'):
            response, validated_data = GetUser(env_config).get_user(user_id, validate=False)
            self.helper.attach_response(response)

        with allure.step('Проверяем статус код'):
            assert response.status_code == 404

        with allure.step('Проверяем что данных нет'):
            assert validated_data is None

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Полное обновление пользователя')
    @allure.testcase("https://jira.example.com/TC-5", "TC-5")
    def test_update_user_put(self, env_config, created_user_ids, cleanup_users):
        with allure.step('Создаем пользователя'):
            response1, validated_data1 = CreateUser(env_config).create_user(
                name="goga",
                job="Alfaker"
            )
            self.helper.attach_response(response1)
            created_user_ids.append(validated_data1.id)
        with allure.step('Проверка статус кода'):
            assert response1.status_code == 201
        for user_id in created_user_ids:
            with allure.step('Редактируем пользователя'):
                response2, validated_data2 = PutUser(env_config).put_user(
                    user_id,
                    name="Artem",
                    job="AQA Engineer"
            )
            self.helper.attach_response(response2)
            with allure.step('Проверяем статус код'):
                assert response2.status_code == 200
            with allure.step('Проверяем измененные данные'):
                assert validated_data2.name == 'Artem'
                assert validated_data2.job == 'AQA Engineer'

    @pytest.mark.regression
    @allure.title('Частичное обновление пользователя')
    @allure.testcase("https://jira.example.com/TC-6", "TC-6")
    def test_update_user_patch(self, env_config, created_user_ids, cleanup_users):
        with allure.step('Создаем пользователя'):
            response1, validated_data1 = CreateUser(env_config).create_user(
                name="goga",
                job="Alfaker"
            )
            self.helper.attach_response(response1)
            created_user_ids.append(validated_data1.id)
        with allure.step('Проверка статус кода'):
            assert response1.status_code == 201
        for user_id in created_user_ids:
            with allure.step('Редактируем пользователя'):
                response2, validated_data2 = PatchUser(env_config).patch_user(
                    user_id,
                    name='Liza'
                )
                self.helper.attach_response(response2)
            with allure.step('Проверяем статус код'):
                assert response2.status_code == 200
            with allure.step('Проверяем измененные данные'):
                assert validated_data2.name == 'Liza'

    @pytest.mark.regression
    @allure.title('Удаление пользователя')
    @allure.testcase("https://jira.example.com/TC-7", "TC-7")
    def test_delete_user(self, env_config):
        with allure.step('Создаем нового пользователя'):
            response1, validated_data1 = CreateUser(env_config).create_user(
                name="Artem",
                job="AQA Engineer"
            )
            self.helper.attach_response(response1)
        with allure.step('Проверяем статус код'):
            assert response1.status_code == 201
        user_id = validated_data1.id
        with allure.step('Удаление пользователя'):
            response2 = DeleteUser(env_config).delete_user(user_id)
        with allure.step('Проверка статус кода'):
            assert response2.status_code == 204
