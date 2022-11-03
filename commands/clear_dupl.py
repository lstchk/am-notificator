from utils.db_util import DbUtil
from utils.bot_manipulator import bot


class ClearDupl:
    def __init__(self, message):
        self.message = message
        self.user = message.chat.id

    def clear(self):
        try:
            db = DbUtil(self.user)
            db.clear_duplicate()
            bot.reply_to(self.message, "Дубликаты удалены")
        except Exception as e:
            bot.reply_to(self.message, "Ошибка обращения к базе данных!")
