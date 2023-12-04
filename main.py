import json
import telebot
import time

from telebot.types import InputFile

API_TOKEN = 'TOKEN'

bot = telebot.TeleBot(API_TOKEN)
# chat_id = ID   # Test Channel
chat_id = 'ID'  # Open Channel

# Handle story


@bot.message_handler(commands=['ch0',
                               'ch1',
                               'ch2',
                               'ch3',
                               'ch3_5',
                               'ch4',
                               'ch5',
                               'ch6',
                               'ch7',
                               'ch8',
                               'ch9',
                               'ch10',
                               'ch11',
                               'ch11_5',
                               'ch12',
                               'ch13',
                               'ch14',
                               'ch15',
                               'ch15_5',
                               'ch15_6',
                               'ch16',
                               'ch17',
                               'ch18',
                               'ch19',
                               'ch19_2',
                               'ch19_5',
                               'ch20',
                               'ch21',
                               'ch21_2',
                               'ch21_3',
                               'ch21_4',
                               'ch22',
                               'ch22_2',
                               'ch22_3',
                               'bonus',
                               'final'])
def send_story(message):
    chapter = message.text.split()[0][1:]
    file = "./story/" + chapter + ".json"
    with open(file) as f:
        data = json.load(f)

    for i in data:
        if i['note'] == 'yes':
            photo_path = './img/' + i['story'] + '.png'
            bot.send_photo(chat_id=chat_id, photo=InputFile(photo_path))
        else:
            bot.send_message(
                chat_id=chat_id,
                text=i['story'],
                parse_mode="MarkdownV2")
        time.sleep(1)


bot.infinity_polling()
