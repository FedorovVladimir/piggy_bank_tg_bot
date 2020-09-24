from Command import Command
from crabs_requests import get, post


def get_categories_menu():
    keys = []
    response = get('/categories')
    for category in response.json():
        keys.append([{'text': category['name'],
                      'callback_data': Command('get_category', '{"id": "' + str(category['id']) + '"}').__str__()}])
    keys.append([{'text': 'Дабавить категорию', "callback_data": Command('add_category').__str__()}])
    keys.append([{'text': 'В меню', "callback_data": Command('menu').__str__()}])
    return {'inline_keyboard': keys}


def add_category(message_text: str):
    response = post('/categories', '{"name": "' + message_text + '"}')
    if response.status_code == 201:
        return 'Категория ' + message_text + ' добавлена'
    else:
        return 'Не удалось добавить категорию'


def get_category_menu(category_id):
    keys = []
    response = get(f'/categories/{category_id}')
    category = response.json()
    keys.append([{'text': 'Удалить категорию',
                  "callback_data": Command('delete_category', '{"id": "' + str(category['id']) + '"}').__str__()}])
