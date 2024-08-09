"""
приложение для продажи товаров в телеграм
"""

import json
from io import BytesIO
from pprint import pprint

import telebot

from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InputFile, \
    Message, CallbackQuery

from db.requests import get_all_routers, update_router_amount

BOT_TOKEN = "TOKEN"

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    upload_file_button = KeyboardButton('Купить')

    markup.row(upload_file_button)

    bot.send_message(message.chat.id, "Добро пожаловать, выберите роутер:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):

    if message.text == 'Купить':
        markup = InlineKeyboardMarkup()
        routers = get_all_routers()
        for router in routers:
            if router.amount >= 1:
                callback_button = InlineKeyboardButton(text=router.name, callback_data=router.name)
                markup.add(callback_button)
        if len(markup.keyboard) == 0:
            bot.send_message(message.chat.id, "Ничего нет в наличии", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Выберите роутер", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: CallbackQuery):
    router_name = call.data
    chat_id = call.message.chat.id

    update_router_amount(router_name, -1)

    bot.send_message(chat_id, "Спасибо за покупку.")


bot.polling(none_stop=True)
