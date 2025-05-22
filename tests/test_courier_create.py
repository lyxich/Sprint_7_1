import allure
import pytest
from pages.courier_page import CourierPage
from utils.helpers import generate_random_string


@allure.feature("Courier Management")
@allure.story("Create Courier")
class TestCourierCreation:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        courier_page = CourierPage()

        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = courier_page.create_courier(payload)

        assert response.status_code == 201
        assert response.json()["ok"] is True

    @allure.title("Нельзя создать курьера без обязательного поля {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_fields(self, missing_field):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        del payload[missing_field]

        courier_page = CourierPage()
        response = courier_page.create_courier(payload)

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_same_courier_twice(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        courier_page = CourierPage()
        response1 = courier_page.create_courier(payload)
        response2 = courier_page.create_courier(payload)

        assert response1.status_code == 201
        assert response2.status_code == 409