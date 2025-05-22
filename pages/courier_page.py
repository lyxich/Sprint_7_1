import requests

class CourierPage:

    def create_courier(self, payload):
        return requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)

    def login_courier(self, payload):
        return requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)

    def delete_courier(self, courier_id):
        return requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}")