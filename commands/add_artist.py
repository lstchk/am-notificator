from telebot import types
from utils.db_util import DbUtil
from utils.bot_manipulator import bot
from utils.spotipy_manipulator import spotify_client


def add_artist_to_db(call, link):
    try:
        user = call.from_user.id
        artist = spotify_client.artist(link)
        artist = artist["name"]
        db = DbUtil(user)
        db.add_new_artist_to_subscribe_list(artist, link)
        bot.reply_to(call.message.chat.id, "Артист добавлен")
    except Exception as e:
        bot.reply_to(call.message.chat.id, "Ошибка обращения к базе данных!")


class AddArtist:
    def __init__(self, message):
        self.message = message
        self.artist = message.text[11:].strip()

    def add(self):
        try:
            results = spotify_client.search(q='artist:' + self.artist, type='artist', limit=3)
            if len(results) > 0:
                items = results['artists']['items']

                artists_pairs = {}
                for item in items:
                    artists_pairs[item['external_urls']['spotify']] = item['name']

                markup = types.InlineKeyboardMarkup()
                # Ссылка-имя
                for link, artist in artists_pairs.items():
                    artist_btn = types.InlineKeyboardButton(text=artist, callback_data="CD1" + link)
                    link_btn = types.InlineKeyboardButton(text=link, url=link)
                    markup.add(artist_btn)
                    markup.add(link_btn)
                bot.send_message(self.message.chat.id, text="Выберите верного артиста", reply_markup=markup)

            else:
                bot.reply_to(self.message, "Данный артист не найден")
        except Exception as e:
            bot.reply_to(self.message, "Ошибка на стороне Spotify API, возможно, заработает позже")
