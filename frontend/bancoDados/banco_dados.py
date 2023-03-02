import mysql.connector

class BancoDados:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def exist_dataBase(self):
        try:

            return True
        except:
            return False
    def connect(self):
        dataBase = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
        cursorObject = dataBase.cursor()
        # creating database if not exists
        cursorObject.execute("CREATE DATABASE IF NOT EXISTS project_rt;")
        cursorObject.close()

        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
