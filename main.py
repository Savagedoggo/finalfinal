import data
import requstlist12345

#вызываем создание нового заказа для получения track
response = requstlist12345.post_new_order(data.order_body)
#тест, вызывающий функцию получения заказа и проверящий код ответа
def test_200():
    user_response = requstlist12345.get_order()
    assert user_response.status_code == 200

