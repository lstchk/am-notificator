from utils.bot_manipulator import bot
from commands.add_artist import AddArtist
from commands.list_artist import ListArtist
from commands.list_albums import ListAlbums



@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """Добавить артиста: /add имя артиста
Список добавленных артистов: /list_artist
Просмотр релизов добавленных артистов: /list_albums 
""")


# add new artist to database
@bot.message_handler(commands=['add'])
def add(message):
    add_artist = AddArtist(message)
    add_artist.add()


@bot.message_handler(commands=['list_artist'])
def list_artists(message):
    artist_list = ListArtist(message)
    artist_list.list()


@bot.message_handler(commands=['list_albums'])
def list_albums(message):
    albums_list = ListAlbums(message)
    albums_list.list()


bot.infinity_polling()
