TOKEN = '1350830739:AAGnYEC2D4XSNoFXFYStaEFBGHJCZGFQM4o'
MESSAGE_ERROR = 'Такого пока не умею('

MESSAGE_START = 'Привет! Я твой помошник по ведению семейного бюджета!\n\nПоказать что я умею?'
KEYBOARD_START = {'inline_keyboard': [
    [{'text': 'Да', "callback_data": "menu"}],
]}

MESSAGE_MENU = 'Вот что я сейчас умею:'
KEYBOARD_MENU = {'inline_keyboard': [
    [{'text': 'Категории', "callback_data": "categories"}],
]}

MESSAGE_CATEGORIES = 'Категории.\n\nВсе ваши доходы/расходы делятся на категории.'

MESSAGE_ADD_CATEGORY = 'Введите название новой категории'
