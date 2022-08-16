import telebot
from telebot import types
from config_reader import ConfigReader

config_reader = ConfigReader("config.json")
config = config_reader.read_config()

#bot = telebot.TeleBot(config['telegram_token'])
bot = telebot.TeleBot("5747313913:AAHzOHw57MtJ29NjLFkD9LVklK45rxuibdc")


def choose_correctly_artist_buttons(artists_pairs):
    for k, i in artists_pairs.items():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton(f"""
                {k}
                {i}
    """)
        markup.add(item)
