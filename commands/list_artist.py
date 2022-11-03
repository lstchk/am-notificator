from utils.db_util import DbUtil
from utils.bot_manipulator import bot


class ListArtist:
    def __init__(self, message):
        self.message = message
        self.user = message.chat.id

    def list(self):
        try:
            db = DbUtil(self.user)
            artist_list = db.export_subscribed_artists()
            res_str = ""
            i = 1
            if len(artist_list)> 0:
                for artist in artist_list:
                    res_str += f"\n{i}) {artist[0]}"
                    i += 1

                bot.reply_to(self.message, res_str)
            else:
                bot.reply_to(self.message, "Список еще пустой, артистов можно добавить с помощью команды /add_artist")
        except Exception as e:
            bot.reply_to(self.message, "Ошибка обращения к базе данных!")
