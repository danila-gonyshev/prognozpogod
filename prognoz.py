import telebot
import requests

API_TOKEN = 'API'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Напиши /pogoda <город>, чтобы узнать погоду.')


def get_pogoda(city):
    url = f'http://wttr.in/{city}?format=3&lang=ru'
    response = requests.get(url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        return 'Город не найден. Попробуй еще раз.'
    
@bot.message_handler(commands=['pogoda'])
def send_pogoda(message):
    try:
        city = message.text.split()[1]
        pogoda_info = get_pogoda(city)
        bot.reply_to(message, pogoda_info)
    except IndexError:
        bot.reply_to(message, 'Пожалуйста, укажите город.')

bot.polling()
