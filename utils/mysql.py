import json
import mysql.connector

configfile = "./config.json"

class MySQL:
    def __init__(self):
        with open(configfile) as f:
            config = json.load(f)

        self.host = config["host"]
        self.user = config["user"]
        self.password = config["password"]
        self.database = config["database"]

    def connect(self):
        return mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database)

    def add_redirect(self, _id: str, url: str):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO urls (id, url) VALUES (%s, %s)", (_id, url))

        connection.commit()
        connection.close()

    def get_redirect(self, _id: str):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("SELECT url FROM urls WHERE id = %s", (_id,))
        result = cursor.fetchone()
        connection.close()
        
        if result is None:
            return None
        else:
            return result[0]

    def delete_redirect(self, _id: str):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM urls WHERE id = %s", (_id,))

        connection.commit()
        connection.close()