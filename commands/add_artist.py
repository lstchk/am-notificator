from telebot import types
from utils.db_util import DbUtil
from utils.bot_manipulator import bot
from utils.spotipy_manipulator import spotify_client


def _find_artist_name(text) -> str:
    artist = text[5:]
    artist = artist.strip()

    return artist


@bot.callback_query_handler(func=lambda call: not None)
def _hand_link(call):
    user = call.from_user.id
    link = call.data
    artist = spotify_client.artist(link)
    artist = artist["name"]
    _add_artist_to_db(user, link, artist)


def _add_artist_to_db(user, link, artist):
    db = DbUtil(user)
    db.add_new_artist_to_subscribe_list(artist, link)


class AddArtist:
    def __init__(self, message):
        self.message = message
        self.artist = _find_artist_name(message.text)

    def add(self):
        results = spotify_client.search(q='artist:' + self.artist, type='artist', limit=3)
        if results['artists']["items"]:
            items = results['artists']['items']

            artists_pairs = {}
            for item in items:
                artists_pairs[item['external_urls']['spotify']] = item['name']

            markup = types.InlineKeyboardMarkup()
            # Ссылка-имя
            for link, artist in artists_pairs.items():
                artist_btn = types.InlineKeyboardButton(text=artist, callback_data=link)
                link_btn = types.InlineKeyboardButton(text=link, url=link)
                markup.add(artist_btn)
                markup.add(link_btn)
            bot.send_message(self.message.chat.id, text="Выберите верного артиста", reply_markup=markup)

        else:
            bot.reply_to(self.message, "Данный артист не найден")
