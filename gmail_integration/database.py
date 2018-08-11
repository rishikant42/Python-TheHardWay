import MySQLdb


class Database:
    def __init__(self, db_host, db_user, db_password, db_name):
        self.connection = MySQLdb.connect(db_host, db_user, db_password, db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, query):
        self.cursor.execute(query)

    def is_table_exist(self, table):
        self.cursor.execute("SHOW TABLES LIKE '{}'".format(table))
        result = self.cursor.fetchone()
        return True if result else False

    def insert_value(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

    def insert_values(self, query, data):
        try:
            self.cursor.executemany(query, data)
            self.connection.commit()
        except:
            self.connection.rollback()

    def fetch(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()
