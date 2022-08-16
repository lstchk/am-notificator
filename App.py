import spotipy
from bot_manipulator import bot
from spotipy.oauth2 import SpotifyClientCredentials
from config_reader import ConfigReader
from add_artist import AddArtist
from list_artist import ListArtist
from list_albums import ListAlbums


config_reader = ConfigReader("config.json")
config = config_reader.read_config()

client_credentials_manager = SpotifyClientCredentials(client_id=config["spotify_client_id"],
                                                      client_secret=config["spotify_secret_key"])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """Добавить артиста: /add имя артиста
Список добавленных артистов: /list_artist
Просмотр релизов добавленных артистов: /list_albums 
""")


@bot.message_handler(commands=['add'])
def add(message):
    add_artist = AddArtist(message, config, sp)
    add_artist.add()


@bot.message_handler(commands=['list_artist'])
def list_artists(message):
    artist_list = ListArtist(bot, config)
    artist_list.list()


@bot.message_handler(commands=['list_albums'])
def list_albums(message):
    albums_list = ListAlbums(bot, config)
    albums_list.list()


bot.infinity_polling()
