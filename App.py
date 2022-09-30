from utils.bot_manipulator import bot
from commands.add_artist import AddArtist
from commands.list_artist import ListArtist
from commands.list_releases import ListReleases
from commands.clear_dupl import ClearDupl


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """Добавить артиста: /add [имя артиста]
Список добавленных артистов: /list_artist
Просмотр релизов добавленных артистов: /list_releases [имя артиста]
Удаление дубликатов в базе данных: /clear_dupl
""")


@bot.message_handler(commands=['add'])
def add(message):
    add_artist = AddArtist(message)
    add_artist.add()


@bot.message_handler(commands=['list_artist'])
def list_artists(message):
    artist_list = ListArtist(message)
    artist_list.list()


@bot.message_handler(commands=['list_releases'])
def list_releases(message):
    albums_list = ListReleases(message)
    albums_list.list()


@bot.message_handler(commands=['clear_dupl'])
def clear_dubl(message):
    cd = ClearDupl(message)
    cd.clear()


bot.infinity_polling()
