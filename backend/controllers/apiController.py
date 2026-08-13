#Logic for what happens when routes are hit

from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError, validates_schema
import  json

from backend.services import database as db

app = Flask(__name__)

class LibrarySchema(Schema):
    songName = fields.Str(required=True)
    albumName = fields.Str(required=True)
    artistName = fields.Str(required=True)
    duration = fields.Int(required=True)
    songYear = fields.Int(required=True)
    songID = fields.Int(required=True)
    albumID = fields.Int(required=True)

    @validates_schema(pass_original=True)
    def validate_required_fields(self,original_data, data, **kwargs):
        required_fields = ['songName', 'albumName', 'artistName', 'duration', 'songYear', 'albumID', 'songID']
        if request.method == 'POST':
            for field in required_fields:
                if field not in data:
                    raise ValidationError(f"Field '{field}' is required.")


library_schema = LibrarySchema()
libraries_schema = LibrarySchema(many=True)

#Album
@app.route('/album/<string:identifier>', methods=['GET', 'DELETE'])
def library_album(identifier):
    albumList = []
    if request.method == 'GET': #GET ALBUM USING ALBUM ID
        album = db.getAlbum(identifier)
        if not album:
            return jsonify({'error': 'Album not found'}), 404
        for albums in album:
            album_item = {'songName': albums['songName'], 'albumName': albums['albumName'], 'artistName':albums['artistName'], 'duration': albums['duration'], 'songYear': albums['songYear'], 'albumID':albums['albumID'], 'songID': albums['songID']}
            albumList.append(album_item)

        return jsonify(albumList), 200

    elif request.method == 'DELETE': #Delete an album
        deleteAlbum = db.deleteAlbum(identifier)
        if not deleteAlbum:
            return jsonify({'error': 'Album not found'}), 404
        return jsonify({'success': 'Album Deleted'}), 202


#
@app.route('/library', methods=['GET', 'POST'])
def library():
    if request.method == 'GET': # get all songs
        library_content = db.getAllLibraries()
        albumList = []
        result = [tuple(row) for row in library_content]
        if not library_content:
            return jsonify({'message': 'Nothing found'}), 404
        for albums in library_content:
            album_item = {'songName': albums['songName'], 'albumName': albums['albumName'],
                          'artistName': albums['artistName'], 'duration': albums['duration'],
                          'songYear': albums['songYear'], 'albumID': albums['albumID'], 'songID': albums['songID']}
            albumList.append(album_item)

        return jsonify(albumList), 200

    elif request.method == 'POST': # add new song to library
        try:
            args = library_schema.load(request.json)
        except ValidationError as err:
            return jsonify({'error': err.messages}), 400
        new_album = db.addToLibrary(args)
        if new_album['message']:
            return jsonify({'message': new_album.message}), 201
        return jsonify({'Message': 'Couldn\'t add to library'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

