from utils.db_util import DbUtil
from utils.bot_manipulator import bot
from telebot import types


def delete_artist_from_db(call, link):
    try:
        user = call.from_user.id
        db = DbUtil(user)
        db.delete_artist(link)
        bot.send_message(call.message.chat.id, "Артист удален")
    except Exception as e:
        bot.reply_to(message, "Ошибка обращения к базе данных!")

class DelArtist:

    def __init__(self, message):
        self.message = message
        self.user = message.chat.id
        self.artist = message.text[12:]

    def delete(self):
        db = DbUtil(self.user)
        artist_list = db.search_artist_from_name(self.artist)

        if len(artist_list) == 0:
            bot.reply_to(self.message, "Данного артиста нет в списке" + self.artist)
        else:
            markup = types.InlineKeyboardMarkup()

            for artist, link in artist_list:
                artist_btn = types.InlineKeyboardButton(text=artist, callback_data="CD2"+link)
                link_btn = types.InlineKeyboardButton(text=link, url=link)
                markup.add(artist_btn)
                markup.add(link_btn)
            bot.send_message(self.message.chat.id, text="Выберите верного артиста", reply_markup=markup)
