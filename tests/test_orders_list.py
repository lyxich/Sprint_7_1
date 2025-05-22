import allure
from pages.order_page import OrderPage


@allure.feature("Orders List")
class TestOrdersList:

    @allure.title("Список заказов доступен")
    def test_get_orders_list(self):
        order_page = OrderPage()
        response = order_page.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()