
from models import db
from flask import Blueprint, jsonify, request
from models import Playlist
from flasgger.utils import swag_from
from swagger_specs import playlist_get_all, playlist_create, playlist_get_by_id, playlist_delete

# Define Blueprint
playlist_bp = Blueprint('playlists', __name__)

@playlist_bp.route('/playlists', methods=['GET'])
@swag_from(playlist_get_all)
def get_playlists():
    playlists = Playlist.query.all()
    result = [
        {
            'id': playlist.id,
            'name': playlist.name,
            'description': playlist.description
        }
        for playlist in playlists
    ]
    return jsonify(result), 200

@playlist_bp.route('/playlists', methods=['POST'])
@swag_from(playlist_create)
def create_playlist():
    data = request.get_json()
    new_playlist = Playlist(
        name=data['name'],
        description=data.get('description', '')
    )
    db.session.add(new_playlist)
    db.session.commit()
    return jsonify({'message': 'Playlist created successfully'}), 201

@playlist_bp.route('/playlists/<int:id>', methods=['GET'])
@swag_from(playlist_get_by_id)
def get_playlist(id):
    playlist = Playlist.query.get_or_404(id)
    songs = [
        {
            'id': ps.song.id,
            'title': ps.song.title,
            'genre': ps.song.genre
        }
        for ps in playlist.songs
    ]
    result = {
        'id': playlist.id,
        'name': playlist.name,
        'description': playlist.description,
        'songs': songs
    }
    return jsonify(result), 200

@playlist_bp.route('/playlists/<int:id>', methods=['DELETE'])
@swag_from(playlist_delete)
def delete_playlist(id):
    playlist = Playlist.query.get_or_404(id)
    db.session.delete(playlist)
    db.session.commit()
    return jsonify({'message': 'Playlist deleted successfully'}), 200
