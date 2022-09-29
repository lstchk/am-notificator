from utils.bot_manipulator import bot
from utils.spotipy_manipulator import spotify_client
from utils.db_util import DbUtil
from utils.config_reader import config


class ListAlbums:
    def __init__(self, message):
        self.message = message
        self.user = message.chat.id

    def list(self):
        conn = DbUtil(self.user)
        artist_list = conn.export_all_releases_from_subscribed_artist()

        for artist in artist_list:
            spotify_client.artist_albums(artist[0])

