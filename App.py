import telebot
from config_reader import ConfigReader
from add_artist import AddArtist
from list_artist import ListArtist
from list_albums import ListAlbums


config_reader = ConfigReader("config.json")
config = config_reader.read_config()

bot = telebot.TeleBot(config['telegram_token'])


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """   Добавить артиста: /add имя артиста
    Список добавленных артистов: /list_artist
    Просмотр релизов добавленных артистов: /list_albums """)


@bot.message_handler(commands=['add'])
def add(message):
    add = AddArtist(bot, config)
    add.add()


@bot.message_handler(commands=['list_artist'])
def list_artists(message):
    list = ListArtist(bot, config)
    list.list()


@bot.message_handler(commands=['list_albums'])
def list_albums(message):
    list = ListAlbums(bot, config)
    list.list()


bot.infinity_polling()
