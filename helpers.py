import random
import string
import requests
import data_burgers


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_registration_body(length):
    registration_body = {}
    registration_body['email'] = f'{generate_random_string(length)}@mail.com'
    registration_body['password'] = generate_random_string(length)
    registration_body['name'] = generate_random_string(length)
    return registration_body


def registration_user_api(body):
    return requests.post(data_burgers.URL_BASE + data_burgers.REGISTER_USER, json=body)


def delete_test_user(token):
    headers = {'Authorization': token}
    return requests.delete(data_burgers.URL_BASE + data_burgers.DATA_USER, headers=headers)
