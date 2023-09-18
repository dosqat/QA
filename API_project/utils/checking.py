"""Методы для проверки запросов"""

import json
from requests import Response

class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code==response.status_code
        if status_code==response.status_code:
            print("Успешно!!! Статус код = " + str(response.status_code))
        else:
            print("Провал!!! Статус код = " + str(response.status_code))

    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(response:Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(response:Response, field_name, expected_value):
        value = response.json().get(field_name)
        assert value== expected_value
        print(field_name + " верен!!!")

    """Метод для проверки значений обязательных полей в ответе запроса по заданному слову"""
    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        value = response.json().get(field_name)
        if search_word in value:
            print("Слово " + search_word + " присутствует!!!")
        else:
            print("Слово " + search_word + " отсутствует!!!")
