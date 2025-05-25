import requests
import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

@allure.step("Регистрация нового курьера через API")
def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    else:
        return []

@allure.step("Создать нового курьера и получить данные")
def register_new_courier():  # Возвращает словарь с данными курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier '
    response = requests.post(url, data=payload)

    if response.status_code == 201:
        return {
            "login": login,
            "password": password,
            "firstName": first_name,
            "id": response.json()["id"]
        }
    else:
        raise Exception(f"Не удалось зарегистрировать курьера. Код: {response.status_code}, Ответ: {response.text}")
