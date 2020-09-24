from crabs_requests import get, post


def get_categories_menu():
    keys = []
    response = get('/categories')
    for category in response.json():
        keys.append([{'text': category['name'], 'callback_data': '{"id": "' + str(category['id']) + '"}'}])
    keys.append([{'text': 'Дабавить категорию', "callback_data": 'add_category'}])
    keys.append([{'text': 'В меню', "callback_data": 'menu'}])
    return {'inline_keyboard': keys}


def add_category(message_text: str):
    response = post('/categories', '{"name": "' + message_text + '"}')
    if response.status_code == 201:
        return 'Категория ' + message_text + ' добавлена'
    else:
        return 'Не удалось добавить категорию'
