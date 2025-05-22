import requests

class OrderPage:

    def create_order(self, payload):
        return requests.post("https://qa-scooter.praktikum-services.ru/api/v1/orders", json=payload)

    def get_orders(self):
        return requests.get("https://qa-scooter.praktikum-services.ru/api/v1/orders")