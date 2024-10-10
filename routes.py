from app import app, db
from models import Playlist
from flask import request, jsonify

# Get all playlists
@app.route('/playlists', methods=['GET'])
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

# Create a new playlist
@app.route('/playlists', methods=['POST'])
def create_playlist():
    data = request.get_json()
    new_playlist = Playlist(
        name=data['name'],
        description=data.get('description', '')
    )
    db.session.add(new_playlist)
    db.session.commit()
    return jsonify({'message': 'Playlist created successfully'}), 201

# Get a specific playlist
@app.route('/playlists/<int:id>', methods=['GET'])
def get_playlist(id):
    playlist = Playlist.query.get_or_404(id)
    result = {
        'id': playlist.id,
        'name': playlist.name,
        'description': playlist.description,
    }
    return jsonify(result), 200

# Delete a playlist
@app.route('/playlists/<int:id>', methods=['DELETE'])
def delete_playlist(id):
    playlist = Playlist.query.get_or_404(id)
    db.session.delete(playlist)
    db.session.commit()
    return jsonify({'message': 'Playlist deleted successfully'}), 200
