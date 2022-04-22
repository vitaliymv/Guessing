import sqlite3
from sqlite3 import Error


class DB:
    def __init__(self):
        self.create_table()

    def insert_value(self, name, score):
        insert_query = f"""INSERT INTO guessing (name, score) 
            VALUES {name, score}
        """
        self.create_connection(insert_query)

    def create_table(self):
        create_table_query = """CREATE TABLE IF NOT EXISTS guessing (
            id INTEGER PRIMARY KEY,
            name VARCHAR(15) NOT NULL,
            score INTEGER NOT NULL
        )"""
        self.create_connection(create_table_query)

    @staticmethod
    def select_value():
        conn = sqlite3.connect("result.db")
        cur = conn.cursor()
        select_query = """SELECT name, score FROM guessing ORDER BY score DESC"""
        try:
            cur.execute(select_query)
            values = cur.fetchall()
            return values
        except Error as e:
            print(f"The error '{e}' occurred")

    def delete_equal_zero(self):
        delete_query = "DELETE FROM guessing WHERE score=0"
        self.create_connection(delete_query)

    @staticmethod
    def return_count():
        conn = sqlite3.connect("result.db")
        cur = conn.cursor()
        count_query = "SELECT COUNT(*) FROM guessing"
        try:
            cur.execute(count_query)
            values = cur.fetchone()[0]
            return values
        except Error as e:
            print(f"The error '{e}' occurred")


    @staticmethod
    def create_connection(query):
        conn = sqlite3.connect("result.db")
        try:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            cur.close()
        except Error as e:
            print(f"The error '{e}' occurred")
