from utils.http_methods import HTTP_methods

"""Методы для тестирования Google maps API"""

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"

class Google_maps_api():

    """Метод для создания новой локации"""
    @staticmethod
    def create_new_location():

        json_create_new_location = {"location": { "lat": -38.383494, "lng": 33.427362 }, "accuracy": 50,
                                     "name": "Frontline house",
                                     "phone_number": "(+91) 983 893 3937",
                                     "address": "29, side layout, cohen 09",
                                     "types": ["shoe park", "shop"],
                                     "website": "http://google.com", "language": "French-IN"}

        post_resource = '/maps/api/place/add/json'
        post_url = base_url + post_resource + key
        print(post_url)

        result_post = HTTP_methods.post(post_url, json_create_new_location)
        print(result_post.text)
        return result_post

    """Метод для проверки созданной локации"""
    @staticmethod
    def get_new_location(place_id):

        get_resouce = '/maps/api/place/get/json'
        get_url = base_url + get_resouce + key + '&place_id=' + place_id
        print(get_url)
        result_get = HTTP_methods.get(get_url)
        print(result_get.text)
        return result_get


    """Метод для изменения созданной локации"""
    @staticmethod
    def update_location(place_id):

        json_update_location = { "place_id": place_id,
                                 "address":"100 Lenina street, RU",
                                 "key":"qaclick123" }

        put_resource = '/maps/api/place/update/json'
        put_url = base_url+put_resource+key
        print(put_url)

        result_put = HTTP_methods.put(put_url,json_update_location)
        print(result_put.text)
        return result_put

    """Метод для изменения созданной локации"""
    @staticmethod
    def delete_location(place_id):

        json_delete = {"place_id": place_id}
        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        print(delete_url)

        result_delete = HTTP_methods.delete(delete_url, json_delete)
        print(result_delete.text)
        return result_delete