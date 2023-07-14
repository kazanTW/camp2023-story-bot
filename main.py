import requests
import schedule
import telebot

from datetime import date, datetime, time
from pytz import timezone

API_TOKEN = 'TOKEN'

bot = telebot.TeleBot(API_TOKEN)
chat_id = -1001967255559
timearea = timezone('Asia/Taipei')

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

# Time getting
@bot.message_handler(commands=['time'])
def send_time():
    time_now = date.today().strftime("%Y-%m-%d")
    bot.send_message(chat_id=chat_id, text=time_now)
    

bot.infinity_polling()
