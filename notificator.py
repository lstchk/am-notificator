from datetime import date
from utils.bot_manipulator import bot
from utils.db_util import DbUtil
from utils.spotipy_manipulator import spotify_client


class Notificator:

    def __init__(self, message):
        self.message = message
        self.user = message.chat.id
        self._search_and_post_new_releases()


    def _search_and_post_new_releases(self):
        db = DbUtil(self.user)
        pairs = db.export_artist_link_pairs()
        for pair in pairs:
            albums = spotify_client.artist_albums(pair[1])
            albums = albums["items"]
            for album in albums:
                if album["release_date"] == str(date.today()):
                    bot.reply_to(self.message, "Новый релиз!\n" + pair[0] + "\n" + album["name"])



