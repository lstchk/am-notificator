from utils.bot_manipulator import bot
from utils.db_util import DbUtil
from utils.spotipy_manipulator import spotify_client


class ListAlbums:
    def __init__(self, message):
        self.message = message
        self.user = message.chat.id
        self.artist = message.text[13:].strip()

    def list(self):
        conn = DbUtil(self.user)
        link_list = conn.export_all_releases_from_artist(self.artist)

        all_releases_list = []
        for link in link_list:
            link = link[0]
            raw = spotify_client.artist_albums(link, limit=50)
            all_releases_list.append(raw)

        res = ""
        for releases_list in all_releases_list:
            releases_list = releases_list["items"]
            for release in releases_list:
                release = release["name"] + " " + release["release_date"]
                res += release + "\n"

        bot.reply_to(self.message, res)
