import telebot
from telebot import types


bot = telebot.TeleBot("5747313913:AAHzOHw57MtJ29NjLFkD9LVklK45rxuibdc")


def choose_correctly_artist_buttons(artists_pairs):
    for k, i in artists_pairs.items():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton(f"""
                {k}
                {i}
    """)
        markup.add(item)
