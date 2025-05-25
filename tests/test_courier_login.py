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

    @allure.feature("Courier Login")
    class TestCourierLogin:

        @allure.title("Невозможно войти без логина")
        def test_login_missing_login(self):
            password = generate_random_string(10)

            payload = {
                "password": password
            }

            courier_page = CourierPage()
            response = courier_page.login_courier(payload)

            assert response.status_code == 400
            assert response.json()["message"] == "Недостаточно данных для входа"

        @allure.title("Невозможно войти без пароля")
        def test_login_missing_password(self):
            login = generate_random_string(10)

            payload = {
                "login": login
            }

            courier_page = CourierPage()
            response = courier_page.login_courier(payload)

            assert response.status_code == 400
            assert response.json()["message"] == "Недостаточно данных для входа"