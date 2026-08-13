#database schema
#from symtable import Class

class Library:
     def __init__(self, id, songName, artistName, albumName, duration, songYear,albumID, songID):
         self.title = songName
         self.artist = artistName
         self.album = albumName
         self.duration = duration
         self.id = id
         self.songYear = songYear
         self.songID = songID
         self.albumID = albumID

