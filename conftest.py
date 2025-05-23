
import pytest
import random
import string
import requests

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def register_new_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier ", data=payload)

    if response.status_code == 201:
        return {
            "login": login,
            "password": password,
            "firstName": first_name,
            "id": response.json()["id"]
        }
    else:
        raise Exception(f"Не удалось зарегистрировать курьера. Код: {response.status_code}, Ответ: {response.text}")

def delete_courier(courier_id):
    response = requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/ {courier_id}")
    return response

@pytest.fixture(scope="function")
def registered_courier():
    """Фикстура создаёт курьера и удаляет его после теста"""
    courier_data = register_new_courier()

    yield courier_data

    # Удаляем курьера после теста
    delete_courier(courier_data["id"])