import sqlite3

CONNECT = sqlite3.connect('music.db')
CURSOR = CONNECT.cursor()


class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album
    
    @classmethod
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        with sqlite3.connect('music.db') as conn:
            conn.execute(sql)
      

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        with sqlite3.connect('music.db') as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (self.name, self.album))
            self.id = cursor.lastrowid
  
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song


Song.create('Hello','25')
CONNECT.commit()