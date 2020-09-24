from Command import Command

TOKEN = '1350830739:AAGnYEC2D4XSNoFXFYStaEFBGHJCZGFQM4o'
MESSAGE_ERROR = 'Такого пока не умею('

MESSAGE_START = 'Привет! Я твой помошник по ведению семейного бюджета!\n\nПоказать что я умею?'
KEYBOARD_START = {'inline_keyboard': [
    [{'text': 'Да', "callback_data": Command("menu").__str__()}],
]}

MESSAGE_MENU = 'Вот что я сейчас умею:'
KEYBOARD_MENU = {'inline_keyboard': [
    [{'text': 'Категории', "callback_data": Command("categories").__str__()}],
]}

MESSAGE_CATEGORIES = 'Категории.\n\nВсе ваши доходы/расходы делятся на категории.'

MESSAGE_ADD_CATEGORY = 'Введите название новой категории'
