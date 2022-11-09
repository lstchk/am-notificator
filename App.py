import time as t
from datetime import datetime, time
from utils.bot_manipulator import bot
from commands.add_artist import AddArtist
from commands.list_artist import ListArtist
from commands.list_releases import ListReleases
from commands.clear_dupl import ClearDupl
from commands.del_artist import DelArtist
from commands import add_artist, del_artist
from notificator import Notificator


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """Добавить артиста: /add_artist [имя артиста]
Список добавленных артистов: /list_artist
Просмотр релизов добавленных артистов: /list_releases [имя артиста]
Включение нотификации:  /start_notification
Удаление дубликатов в базе данных: /clear_dupl
Удаление артиста из списка: /del_artist [имя артиста]
Так же команды можно посмотреть в меню бота
""")


@bot.message_handler(commands=['add_artist'])
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


@bot.message_handler(commands=['del_artist'])
def del_artist(message):
    dl = DelArtist(message)
    dl.delete()


@bot.message_handler(commands=['start_notification'])
def start_notification(message):
    bot.reply_to(message, "Подписка оформлена!")
    while True:
        dt = datetime.now().time()
        s_dt = time(7, 0, 0)
        e_dt = time(7, 1, 0)
        if dt > s_dt and e_dt > dt:
            n = Notificator(message)
            t.sleep(86400)


@bot.callback_query_handler(func=lambda call: not None)
def _hand_link(call):
    data = call.data
    callback_code = data[:3]
    pure_data = data[3:]
    if callback_code == "CD1":
        add_artist.add_artist_to_db(call, pure_data)
    elif callback_code == "CD2":
        del_artist.delete_artist_from_db(call, pure_data)


bot.infinity_polling()
