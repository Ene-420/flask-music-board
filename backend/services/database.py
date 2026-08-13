#Business Logic to talk to DB

from backend.config import dbConnection
from flask import Flask

app = Flask(__name__)
app.config['DATABASE'] = '../config/test.db'


def addToLibrary(library):
    #cursor, connection = dbConnection.callDB()
    db = dbConnection.get_db()
    cursor = db.cursor()



    add_to_library = '''
            INSERT INTO library(songName, albumName, artistName, songID, albumID, duration, songYear)
            VALUES (?,?,?,?,?,?,?);
    '''
    cursor.execute(add_to_library, (library['songName'], library['albumName'], library['artistName'],library['songID'], library['albumID'], library['duration'], library['songYear']))
    db.commit()
    return {'message': 'success'}

# DELETE ALBUM
def deleteSong(songID):
    db = dbConnection.callDB_PARSED()
    cursor = db.cursor()

    delete_from_library = '''
        DELETE FROM library
        WHERE songID = ?;
    '''

    cursor.excute(delete_from_library, (songID))
    db.commit()

def deleteAlbum(albumID):
    db = dbConnection.get_db()
    cursor = db.cursor()

    delete_from_library = '''
        DELETE FROM library
        WHERE albumID = ?;
    '''

    cursor.excute(delete_from_library, (albumID))
    db.commit()

def getAllLibraries():
    with app.app_context():
        db = dbConnection.get_db()
        cursor = db.cursor()

        get_all_libraries = '''
        SELECT * FROM library;
        '''

        cursor.execute(get_all_libraries)

        return cursor.fetchall()

def getAlbum(albumID):
    db = dbConnection.get_db()
    cursor = db.cursor()

    get_album = '''
        SELECT * FROM library
        WHERE albumID = ?;
    '''

    cursor.execute(get_album, (albumID,))

    return cursor.fetchall()

def getSong(songID):
    db = dbConnection.get_db()
    cursor = db.cursor()
    get_song= '''
        SELECT * FROM library
        WHERE songID = ?;
    '''

    cursor.execute(get_song, (songID))
    return cursor.fetchone()

def getAllArtistSongs(artistName):
    db = dbConnection.get_db()
    cursor = db.cursor()

    get_all_artists_songs = '''
        SELECT * FROM library
        WHERE artistName = ?;
    '''

    cursor.execute(get_all_artists_songs, (artistName))

    return cursor.fetchall()


def getAllSingles():
    db = dbConnection.get_db()
    cursor = db.cursor()

    get_all_singles = '''
        SELECT * FROM library WHERE albumName REGEGEXP "? - Single"
    '''

if __name__ == '__main__':
    for  item in getAllLibraries():
        print(f'{item['songName']} by {item['artistName']} in {item['albumName']}')