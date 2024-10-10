from app import app, db
from models import Playlist, Song, PlaylistSong
from flask import request, jsonify
from sqlalchemy import text

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

# Delete a playlist
@app.route('/playlists/<int:id>', methods=['DELETE'])
def delete_playlist(id):
    playlist = Playlist.query.get_or_404(id)
    db.session.delete(playlist)
    db.session.commit()
    return jsonify({'message': 'Playlist deleted successfully'}), 200

@app.route('/songs', methods=['GET'])
def get_songs():
    songs = Song.query.all()
    result = [
        {
            'id': song.id,
            'name': song.title,
            'genre': song.genre
        }
        for song in songs
    ]
    return jsonify(result), 200

# Create a new playlist
@app.route('/songs', methods=['POST'])
def create_song():
    data = request.get_json()
    new_song = Song(
        title=data['title'],
        genre=data.get('genre', '')
    )
    db.session.add(new_song)
    db.session.commit()
    return jsonify({'message': 'Song created successfully'}), 201


# Add a song to a playlist
@app.route('/playlists/<int:id>/songs', methods=['POST'])
def add_song_to_playlist(id):
    data = request.get_json()
    song_id = data['song_id']
    playlist = Playlist.query.get_or_404(id)
    song = Song.query.get_or_404(song_id)

    existing_entry = PlaylistSong.query.filter_by(
        playlist_id=playlist.id, song_id=song.id
    ).first()

    if existing_entry:
        return jsonify({'message': 'Song already in playlist'}), 400

    new_entry = PlaylistSong(playlist_id=playlist.id, song_id=song.id)
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({'message': 'Song added to playlist'}), 201

# Remove a song from a playlist
@app.route('/playlists/<int:playlist_id>/songs/<int:song_id>', methods=['DELETE'])
def remove_song_from_playlist(playlist_id, song_id):
    entry = PlaylistSong.query.filter_by(
        playlist_id=playlist_id, song_id=song_id
    ).first_or_404()
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Song removed from playlist'}), 200


# Get playlists containing songs of a specific genre
@app.route('/playlists/genre/<string:genre>', methods=['GET'])
def get_playlists_by_genre(genre):
    sql_query = text("""
    SELECT DISTINCT playlist.id, playlist.name, playlist.description
    FROM playlist
    JOIN playlist_song ON playlist.id = playlist_song.playlist_id
    JOIN song ON song.id = playlist_song.song_id
    WHERE song.genre = :genre
    """)
    result = db.session.execute(sql_query, {'genre': genre})
    rows = result.mappings().all()

    playlists = [
        {
            'id': row['id'],
            'name': row['name'],
            'description': row['description']
        }
        for row in rows
    ]
    return jsonify(playlists), 200
