import os, sys
activate_this = '/home/bot/python/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я жив!')

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.reply_to(message, message.text)

bot.polling(none_stop=True, interval=0)
