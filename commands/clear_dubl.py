from utils.db_util import DbUtil


class ClearDubl:
    def __init__(self, message):
        self.message = message
        self.user = message.chat.id

    def clear(self):
        db = DbUtil(self.user)
        db.clear_dublicate()
