import telebot
from telebot import types
import random

insults = ['ИДИОТ', 'ИНВАЛИД', 'ПРИДУРОК', 'ОБРУБОК', 'ДАУН']

photos = ['https://i.ytimg.com/vi/G16WExzpjqU/maxresdefault.jpg', 'https://funik.ru/wp-content/uploads/2020/11/0b7c8c5cf92604e7dd47-1.jpg', 'https://i.ytimg.com/vi/EyacUTt4bPs/maxresdefault.jpg', 'https://webmg.ru/wp-content/uploads/2022/09/i-41-26.jpeg']

bot = telebot.TeleBot('7031359148:AAEb7px-pAK6g52d4mkmdeWjLUhnasTD_x0')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Напиши /help, если не знаешь что делать')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Бот Андрей - это уникальный бот со своим юмором и стилем. Для того, чтобы узнать его функции напиши /button')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Оскорбление от МЕНЯ")
    item2=types.KeyboardButton('Мемы')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id,'Выбирайте!',reply_markup=markup)


@bot.message_handler(content_types='text')
def func(message):
    if message.text == 'Мемы':
        meme0 = random.choice(photos)
        bot.send_photo(message.chat.id, meme0)
        if meme0 == photos[-2]:
            bot.send_message(message.chat.id, 'Поздравляю! Тебе выпала легендарная картинка "Mr. Андрей Брос (в старости)"')
    elif message.text == 'Оскорбление от МЕНЯ':
        ainsult = random.choice(insults)
        bot.send_message(message.chat.id, ainsult)

    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю, Обрубок. Либо мемы, либо оскорбления!!!')
        button_message(message)


bot.polling(none_stop=True)