import mariadb
from utils.config_reader import config
from utils.bot_manipulator import bot


class DbUtil:

    def __init__(self, user):
        self.conn = mariadb.connect(
            user=config['mariadb_user'],
            password=config["mariadb_password"],
            host=config["mariadb_host"],
            port=config["mariadb_port"],
            database=config["mariadb_database"]
        )
        self.user = user
        self.cursor = self.conn.cursor()

    def add_new_artist_to_subscribe_list(self, artist_name, sp_link):
        ex_str = f"INSERT INTO subscribe(user, artist, link) VALUES ('{self.user}', '{artist_name}', '{sp_link}') "
        try:
            self.cursor.execute(ex_str)
            print(ex_str, 'ok')
            self.conn.commit()
            bot.send_message(self.user, text="Артист добавлен")
        except mariadb.Error as e:
            print(f"Error to add new artist in subscribe\n {e}")
            bot.send_message(self.user, text="Ошибка при добавлении исполнителя")

        self.conn.close()

    def export_all_releases_from_artist(self, artist):
        ex_str = f"SELECT link FROM subscribe WHERE user = '{self.user}' AND artist = '{artist}'"
        link_list = []
        try:
            self.cursor.execute(ex_str)
            link_list = self.cursor.fetchall()
        except mariadb.Error as e:
            bot.send_message(self.user, text="Ошибка при экспорте релизов")
            print(f"Error load data from subscribe\n {e}")

        self.conn.close()

        return link_list

    def export_subscribed_artists(self):
        ex_str = f"SELECT artist FROM subscribe WHERE user = '{self.user}'"
        self.cursor.execute(ex_str)
        artists_list = self.cursor.fetchall()

        return artists_list

    def clear_duplicate(self):
        ex_str = "ALTER IGNORE TABLE subscribe ADD UNIQUE KEY(`user`, `artist`, `link`)"
        self.cursor.execute(ex_str)
