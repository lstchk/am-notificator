from utils.bot_manipulator import bot
from utils.db_util import DbUtil
from utils.spotipy_manipulator import spotify_client


class ListReleases:
    def __init__(self, message):
        self.message = message
        self.user = message.chat.id
        self.artist = message.text[14:].strip()

    def list(self):
        try:
            conn = DbUtil(self.user)
            link_list = conn.export_all_releases_from_artist(self.artist)
        except Exception as e:
            bot.reply_to(self.message, "Ошибка обращения к базе данных!")
        if len(link_list) > 0:
            for link in link_list:
                link = link[0]
                try:
                    albums = spotify_client.artist_albums(link, album_type="album", limit=50)
                    singles = spotify_client.artist_albums(link, album_type="single", limit=50)
                    compilations = spotify_client.artist_albums(link, album_type="compilation", limit=50)
                    feats = spotify_client.artist_albums(link, album_type="appears_on", limit=50)

                    albums = albums["items"]
                    singles = singles["items"]
                    compilations = compilations["items"]
                    feats = feats["items"]

                    res = f"Релизы {self.artist}:\n"
                    res += "Альбомы:\n"
                    res = self._add_releases_to_message(res, albums)
                    res += "\n"
                    res += "EP и Синглы:\n"
                    res = self._add_releases_to_message(res, singles)
                    res += "\n"
                    res += "Компиляции:\n"
                    res = self._add_releases_to_message(res, compilations)
                    res += "\n"
                    res += "Фиты:\n"
                    res = self._add_releases_to_message(res, feats)

                    if len(res) < 4096:
                        bot.reply_to(self.message, res)
                    else:
                        while len(res) != 0:
                            cut_res = res[:4095]
                            res = res[4095:]
                            bot.reply_to(self.message, cut_res)
                except Exception as e:
                    bot.reply_to(self.message, "Ошибка на стороне Spotify API, возможно, заработает позже")
        else:
            bot.reply_to(self.message, "В списке нет такого артиста")

    def _add_releases_to_message(self, res, releases):
        for release in releases:
            release = release["name"] + " " + release["release_date"]
            res += release + "\n"

        return res
