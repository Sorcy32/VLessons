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
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {    'proxy_url': 'socks5://t1.learn.python.ru:1080',    'urllib3_proxy_kwargs': {
        'username': 'learn',         'password': 'python'    }}

def planet(bot, update):
    print("new")

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text("Введи /planet название планеты: ")


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
    if user_text == "/planet Mars":
        planet(bot, update)
 

def main():
    mybot = Updater("871351306:AAGjqZ1sX53ZFjd0tkj5NPuvk5XI4XwULAM", ) #request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
