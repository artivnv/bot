"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import datetime
import logging
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
level=logging.INFO,
filename='bot.log')

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot, update):
    text = 'Вызвана команда start'
    print(text)
    update.message.reply_text(text)

def greet_planet(bot, update):
    text = 'Вызвана команда planet'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def user_planet(bot, update):
    user_text = update.message.text.split(' ')[1]
    if user_text == 'Moon':
        p = ephem.Moon(datetime.date.today())
    elif user_text == 'Saturn':
        p = ephem.Saturn(datetime.date.today())
    elif user_text == 'Jupiter':
        p = ephem.Jupiter(datetime.date.today())
    else:
        return 0
    try:
        answer = ephem.constellation(p)
    except Exception:
        answer = "Нет данных об этом небесном теле."
    planet_names = {
    'Aries': 'Овен', 'Taurus': 'Телец', 'Gemini': 'Близнецы', 'Cancer': 'Рак', 'Leo': 'Лев',
    'Virgo': 'Дева', 'Libra': 'Весы', 'Scorpio': 'Скорпион', 'Sagittarius': 'Стрелец',
    'Capricornus': 'Козерог', 'Aquarius': 'Водолей', 'Pisces': 'Рыбы',
    }
    update.message.reply_text(f'На текущую дату, небесное тело находится в созвездии {planet_names[answer[1]]}.')

def main():
    mybot = Updater('1054374108:AAGvvQwpLz2d_lf6TjsGrwm-ed-2EF1HMFc',request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", user_planet))
    mybot.start_polling()
    mybot.idle()
main()






