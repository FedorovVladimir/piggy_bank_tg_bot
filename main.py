import asyncio

import telepot
from telepot.loop import MessageLoop

from env import TOKEN, MESSAGE_ERROR, MESSAGE_START, KEYBOARD_START, MESSAGE_MENU, KEYBOARD_MENU, MESSAGE_CATEGORIES, \
    MESSAGE_ADD_CATEGORY
from ruls import get_categories_menu, add_category

bot = telepot.Bot(TOKEN)

state = 'normal'


def handle(message):
    global state

    if "text" in message:
        chat_id = message["chat"]["id"]
        message_text = message["text"]
    elif "data" in message:
        chat_id = message["message"]["chat"]["id"]
        message_text = message["data"]
    else:
        chat_id = message["chat"]["id"]
        bot.sendMessage(chat_id, MESSAGE_ERROR)
        return

    if state == 'normal':
        if message_text == "/start":
            bot.sendMessage(chat_id, MESSAGE_START, reply_markup=KEYBOARD_START)
        if message_text == 'menu':
            bot.sendMessage(chat_id, MESSAGE_MENU, reply_markup=KEYBOARD_MENU)
        if message_text == 'categories':
            bot.sendMessage(chat_id, MESSAGE_CATEGORIES, reply_markup=get_categories_menu())
        if message_text == 'add_category':
            state = 'add_category'
            bot.sendMessage(chat_id, MESSAGE_ADD_CATEGORY)
    elif state == 'add_category':
        state = 'normal'
        text = add_category(message_text)
        bot.sendMessage(chat_id, text, reply_markup=get_categories_menu())


# цикл приема сообщений
loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot, handle).run_forever())
loop.run_forever()
