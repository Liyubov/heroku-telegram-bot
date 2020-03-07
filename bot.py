https://github.com/Liyubov/heroku-telegram-bot# -*- coding: utf-8 -*-
import redis
import os
import telebot

# import some_api_lib
# import ... #uncomment and add other additions

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']   #

#some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
#r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...


from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler


updater = Updater(token = tok_bot, use_context=True)

dispatcher = updater.dispatcher

#for logs and errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#function for specific start communication
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    

#start command 
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
    
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=" Please insert how many hours did you sleep today. It is better if you do it regularly every morning... ")  
    

    
