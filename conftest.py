import pytest
from utils.helpers import register_new_courier_and_return_login_password


@pytest.fixture(scope="function")
def registered_courier():
    """Регистрирует нового курьера и возвращает его логин и пароль"""
    return register_new_courier_and_return_login_password()