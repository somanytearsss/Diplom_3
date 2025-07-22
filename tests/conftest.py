import pytest
import allure
from selenium import webdriver

import src.config
from helpers import *
from src.config import Urls

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    else:
        driver = webdriver.Firefox()
    driver.get(src.config.Urls.MAIN_URL)
    yield driver
    driver.quit()

@pytest.fixture
@allure.title('Создание и удаление тестового пользователя')
def create_and_delete_user():
    payload, response = auth_user_and_get_creds()
    email = payload.get('email')
    password = payload.get('password')
    yield email, password
    access_token = response.json().get('accessToken')
    requests.delete(f'{Urls.DELETE_USER_URL}', headers={'Authorization': access_token})