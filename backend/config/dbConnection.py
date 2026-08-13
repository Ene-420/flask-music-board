#DB connection
from flask import g, current_app, Flask
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test.db")

app = Flask(__name__)
app.config['DATABASE'] = db_path

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def callDB_PARSED():
    with app.app_context():
        db  = get_db()
        cursor  = db.cursor()

        cursor.execute('''
            SELECT * FROM Library
        ''')
        return cursor.fetchone()

def callDB():
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        print("Database created and connected successfully")

        return cursor, connection

        # create_table_query = '''
        #     CREATE TABLE IF NOT EXISTS library (
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         songName TEXT NOT NULL,
        #         albumName TEXT NOT NULL,
        #         artistName TEXT NOT NULL,
        #         songID INTEGER NOT NULL,
        #         albumID INTEGER NOT NULL,
        #         duration INTEGER NOT NULL,
        #         songYear INTEGER NOT NULL
        #     );
        # '''



#library -> ID, songName, albumName,artistName,songID,albumID, duration, SongYear

        create_table_insertion = '''
        
        '''

        list = [
            ('Bound 2', 'Yeezus', 'Kanye West', 10,  1,  120,  2012),
            #( '90210',  'Rodeo', 'Travis Scott', 9, 3, 145,  20169),
            #('Psycho',  'Pyscho - Single', 'SlowThai Ft. Denzel Curry',  10, 7009,  120,  2015),
            #('U', 'To Pimp A Butterfly',  'Kendrick Lamar',  5, 6699,  120,  2015),
        ]

        # for items in list:
        #     query = '''
        #         INSERT INTO library(songName, albumName, artistName, songID, albumID, duration, songYear)
        #         VALUES (?,?,?,?,?,?,?);
        #     '''
        #     cursor.execute(query, items)
        #
        # connection.commit()

        # select_query = "SELECT * FROM Library"
        #
        # cursor.execute(select_query)
        #
        # for row in cursor.fetchall():
        #     print(row)






if __name__ == '__main__':
    #callDB()
    item =  callDB_PARSED()
    print("Database created and connected successfully\n")
    print(f'{item['songName']} by {item['artistName']} in {item['albumName']}')