import sqlite3


class SQLite:
    db = None

    def __init__(self, db):
        self.db = sqlite3.connect(db)

    def version(self):
        cur = self.db.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print("SQLite version: %s" % data)

    def fetch(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        return cursor

    def execute(self, query, iterable=None):
        cursor = self.db.cursor()
        if iterable:
            cursor.execute(query, iterable)
        else:
            cursor.execute(query)
        self.db.commit()

    def __exit__(self):
        self.db.close()
