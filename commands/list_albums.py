from utils.bot_manipulator import bot
from utils.spotipy_manipulator import spotify_client
from utils.db_util import DbUtil
from utils.config_reader import config
#import pandas as pd


class ListAlbums:
    def __init__(self, message):
        self.message = message

    def list(self):
        conn = DbUtil(self.message.chat.id, self.message.from_user.id)
        artist_list = conn.export_all_releases_from_subscribed_artist()

        for artist in artist_list:
            spotify_client.artist(artist)
