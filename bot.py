from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
level=logging.INFO,
filename='bot.log'
)

def greet_user(bot, update):
   text = 'Вызван /start'
   print(text)
   update.message.replay_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater('1054374108:AAGvvQwpLz2d_lf6TjsGrwm-ed-2EF1HMFc',request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()
main()







