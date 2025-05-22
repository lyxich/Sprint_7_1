import allure
import pytest
import requests
from pages.courier_page import CourierPage
from utils.helpers import generate_random_string

@allure.feature("Courier Login")
class TestCourierLogin:

    @allure.title("Курьер может авторизоваться")
    def test_courier_login_success(self, registered_courier):
        if not registered_courier:
            pytest.fail("Не удалось зарегистрировать курьера")

        courier_page = CourierPage()
        payload = {"login": registered_courier[0], "password": registered_courier[1]}
        response = courier_page.login_courier(payload)

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Ошибка при неверном логине или пароле")
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_courier_login_invalid_credentials(self, wrong_field, registered_courier):
        if not registered_courier:
            pytest.fail("Не удалось зарегистрировать курьера")

        payload = {"login": registered_courier[0], "password": registered_courier[1]}
        payload[wrong_field] += "wrong"

        courier_page = CourierPage()
        response = courier_page.login_courier(payload)

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Ошибка при отсутствии обязательного поля {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_login_missing_field(self, missing_field):
        login = generate_random_string(10)
        password = generate_random_string(10)

        payload = {
            "login": login,
            "password": password
        }

        if missing_field in payload:
            del payload[missing_field]

        courier_page = CourierPage()
        response = courier_page.login_courier(payload)

        assert response.status_code in [400, 504], f"Получен неожиданный статус-код: {response.status_code}"

        try:
            json_data = response.json()
            assert "message" in json_data
        except requests.exceptions.JSONDecodeError:
            # Если ответ не в формате JSON — проверяем, что статус 504
            assert response.status_code == 504, "Должен быть 504, если ответ не JSON"