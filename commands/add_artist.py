from telebot import types
from utils.db_util import DbUtil
from utils.bot_manipulator import bot
from utils.spotipy_manipulator import spotify_client

artists_pairs = {}


def _find_artist_name(text) -> str:
    artist = text[5:]
    artist = artist.strip()

    return artist


class AddArtist:
    def __init__(self, message):
        self.message = message
        self.artist = _find_artist_name(message.text)

    def add(self):
        results = spotify_client.search(q='artist:' + self.artist, type='artist', limit=3)
        if results['artists']["items"]:
            items = results['artists']['items']
            self._create_artist_url_pairs(items)
            i = 1
            markup = types.InlineKeyboardMarkup()
            for k, v in artists_pairs.items():
                artist = types.InlineKeyboardButton(text=v, callback_data=k)
                link = types.InlineKeyboardButton(text=k, url=k)
                markup.add(artist)
                markup.add(link)
                i += 1
            bot.send_message(self.message.chat.id, text="Выберите верного артиста", reply_markup=markup)
        else:
            bot.reply_to(self.message, "Данный артист не найден")

    def _create_artist_url_pairs(self, items) -> dict:
        for i in items:
            artists_pairs[i['external_urls']['spotify']] = i['name']

    @bot.callback_query_handler(func=lambda call: True)
    def _handle_artist_callback(self, call):
        bot.answer_callback_query(callback_query_id=call.id)
        answer = call.data
        db = DbUtil(self.message.chat.id, call.from_user.id)
        db.add_new_artist_to_subscribe_list(artists_pairs[answer], answer)
