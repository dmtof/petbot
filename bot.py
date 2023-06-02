import os, sys
activate_this = '/home/bot/python/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

import telebot
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, какая у вас проблема?')
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('1....')
    item2 = types.KeyboardButton('2....')
    item3 = types.KeyboardButton('3....')
    item4 = types.KeyboardButton('4....')
    item5 = types.KeyboardButton('5....')