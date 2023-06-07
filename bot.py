import os, sys
activate_this = '/home/bot/python/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

questions = [
    'Как вас зовут?',
    'Где вы живёте?',
    'Какая категория услуг Вам требуется? (Напишите цифру ответа)\n\n1: Ремонт и строительство\n2: Уборка и помощь по хозяйству\n3: Грузоперевозки\n4: Установка и ремонт техники\n5: Красота и здоровье\n6: Ремонт транспорта',
    'Опишите требуемую услугу'
]

answers = {}

@bot.message_handler(commands=['start'])
def start(message):
    answers.clear()
    bot.send_message(message.chat.id, 'Добро пожаловать! Ответьте на первый вопрос:')
    bot.send_message(message.chat.id, questions[0])

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    current_question = len(answers) + 1

    if current_question == 3:
        if message.text.isdigit() and 1 <= int(message.text) <= 6:
            answers[current_question] = message.text
            bot.send_message(message.chat.id, 'Ответ принят. Ответьте на следующий вопрос:')
            bot.send_message(message.chat.id, questions[current_question])
        else:
            bot.send_message(message.chat.id, 'Пожалуйста, выберите вариант ответа, введя соответствующую цифру.')
    elif current_question <= len(questions):
        answers[current_question] = message.text

        if current_question == len(questions):
            send_application(message.chat.id)
        else:
            bot.send_message(message.chat.id, 'Ответ принят. Ответьте на следующий вопрос:')
            bot.send_message(message.chat.id, questions[current_question])
    else:
        bot.send_message(message.chat.id, 'Вы уже ответили на все вопросы.')

def send_application(chat_id):
    category_mapping = {
        '1': 'Ремонт и строительство',
        '2': 'Уборка и помощь по хозяйству',
        '3': 'Грузоперевозки',
        '4': 'Установка и ремонт техники',
        '5': 'Красота и здоровье',
        '6': 'Ремонт транспорта'
    }

    category = category_mapping.get(answers[3], 'Неизвестная категория')

    application = ''
    for question_number, answer in answers.items():
        application += f'{questions[question_number - 1]}\n'
        if question_number == 3:
            application += f'Ответ: {category}\n\n'
        else:
            application += f'Ответ: {answer}\n\n'

    bot.send_message('-1001932793631', application)
    bot.send_message(chat_id, 'Спасибо! Ваша заявка отправлена.')

bot.polling()
