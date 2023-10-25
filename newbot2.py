import telebot
from telebot import types  
import requests

token = "6977791885:AAHdWeyP4VYjLyFo3ncZsfH8F9m230AP1zY"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Location', request_location=True)
    keyboard.add(button1)
    bot.send_message(message.chat.id, 'Welcome to our bot', reply_markup=keyboard)

api = '36c55687e20d4d09aa7114432232310'
@bot.message_handler(content_types=['location'])
def handle_location(message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    url = f'http://api.weatherapi.com/v1/current.json?key={api}&q={latitude},{longitude}'
    response = requests.get(url)
    a = response.json().get('current').get('temp_c')
    b = response.json().get('location').get('region')
    c = response.json().get('location').get('country')
    d = response.json().get('current').get('last_updated')
    e = response.json().get('current').get('condition').get("text")
    photo = response.json().get('current').get('condition').get('icon')
    photo_url = f'https:{photo}'
    bot.send_message(message.chat.id, f"Region: {b} \n\nCountry: {c} \n\nThe temperature: {a} \n\nLast_update: {d} \n\nCondition: {e} \n\n")
    bot.send_photo(message.chat.id, photo_url)
    

if __name__ == '__main__':
    bot.infinity_polling()
