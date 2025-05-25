import pytest
from utils.helpers import register_new_courier, delete_courier


@pytest.fixture(scope="function")
def registered_courier():
    """Фикстура создаёт курьера и удаляет его после теста"""
    courier_data = register_new_courier()

    yield courier_data

    # Удаляем курьера после выполнения теста
    delete_courier(courier_data["id"])