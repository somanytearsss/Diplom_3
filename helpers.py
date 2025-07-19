import random
import string
import requests
from src.config import Urls



def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_random_email_password_name():
    # создаём словарь, чтобы метод мог его вернуть
    payload = {}

    # генерируем email, пароль и имя пользователя
    payload['email'] = f'test-{generate_random_string(7)}@yandex.ru'
    payload['password'] = generate_random_string(7)
    payload['name'] = generate_random_string(7)

    return payload

def auth_user_and_get_creds():
    payload = generate_random_email_password_name()
    response = requests.post(f'{Urls.CREATE_USER_URL}', json=payload)
    return payload, response

def get_access_token(response):
    return response.json().get('accessToken')