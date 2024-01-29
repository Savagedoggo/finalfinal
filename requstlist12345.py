import configuration
import requests
import data
#глобальная переменная для трек номера
track1 = ""
#создаем заказ и записываем трек-номер в глобальную переменную
def post_new_order(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                             json=body,
                             headers=data.headers)
    global track1
    track1 = response.json()["track"]
    return response
#получаем заказ 
def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track1))

