import psycopg2
from config import settings

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_HOST,
            port=settings.DB_PORT
        )
        self.cur = self.conn.cursor()

    def execute(self, query, values=None):
        self.cur.execute(query, values)
        self.conn.commit()

    def fetchone(self, query, values=None):
        self.cur.execute(query, values)
        return self.cur.fetchone()

    def fetchall(self, query, values=None):
        self.cur.execute(query, values)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()
