import requests
import allure

class OrderPage:

    @allure.step("Создать заказ с данными {payload}")
    def create_order(self, payload):
        return requests.post("https://qa-scooter.praktikum-services.ru/api/v1/orders", json=payload)

    @allure.step("Создать заказ с данными {payload}")
    def get_orders(self):
        return requests.get("https://qa-scooter.praktikum-services.ru/api/v1/orders")