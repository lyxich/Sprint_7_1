import requests
import allure
class CourierPage:

    @allure.step("Создать курьера с данными {payload}")
    def create_courier(self, payload):
        return requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)

    @allure.step("Войти как курьер с данными {payload}")
    def login_courier(self, payload):
        return requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data=payload)

    @allure.step("Удалить курьера с ID {courier_id}")
    def delete_courier(self, courier_id):
        return requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}")