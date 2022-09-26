import mariadb
from config_reader import config
from bot_manipulator import bot

class DbUtil:

    def __init__(self, user_id, chat_id):
        self.conn = mariadb.connect(
            user=config['mariadb_user'],
            password=config["mariadb_password"],
            host=config["mariadb_host"],
            port=config["mariadb_port"],
            database=config["mariadb_database"]
        )
        self.user_id = user_id
        self.cursor = self.conn.cursor()
        self.chat_id = chat_id

    def add_new_artist_to_subscribe_list(self, artist, link):
        ex_str = f"INSERT INTO {config['subscribe_table']} VALUES ({artist}, {link}, {self.user_id})"

        try:
            self.cursor.execute(ex_str)
        except mariadb.Error as e:
            print(f"Error to add new artist in {config['subscribe_table']}")
            bot.send_message(self.message.chat.id, text="Ошибка при добавлении исполнителя")

        self.conn.close()
