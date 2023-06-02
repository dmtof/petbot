import os, sys
activate_this = '/home/bot/python/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('first')
    item2 = types.KeyboardButton('second')
    item3 = types.KeyboardButton('third')
    item4 = types.KeyboardButton('fourth')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.reply_to(message, message.text)

bot.polling(none_stop=True, interval=0)