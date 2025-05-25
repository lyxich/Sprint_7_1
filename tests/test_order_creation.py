import allure
import pytest
from pages.order_page import OrderPage


@allure.feature("Order Creation")
class TestOrderCreation:

    @allure.title("Создание заказа с цветом {color}")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order_with_color(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha"
        }
        if color:
            payload["color"] = color

        order_page = OrderPage()
        response = order_page.create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()