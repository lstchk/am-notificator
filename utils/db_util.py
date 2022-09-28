  GNU nano 6.2                                                                                                   utils/db_util.py                                                                                                            import mariadb
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
        except mariadb.Error as e:
            print(f"Error to add new artist in {config['subscribe_table']}\n {e}")
            bot.send_message(self.user, text="Ошибка при добавлении исполнителя")

        self.conn.close()

    def export_all_releases_from_subscribed_artist(self):
        ex_str = f"SELECT name FROM {config['subscribe_table']} WHERE user_id = '{self.user}"

        try:
            artist_list = self.cursor.execute(ex_str)
        except mariadb.Error as e:
            bot.send_message(self.user, text="Ошибка при экспорте альбомов")
            print(f"Error load data from {config['subscribe_table']}\n {e}")
        self.conn.close()

        return artist_list