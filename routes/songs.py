from models import Artist, db
from flask import Blueprint, jsonify, request
from models import Song, Playlist, PlaylistSong
from flasgger.utils import swag_from
from sqlalchemy import text
from swagger_specs import song_get_all, song_create, add_song_to_playlist, remove_song_from_playlist, songs_by_artist, songs_by_genre

song_bp = Blueprint('songs', __name__)

@song_bp.route('/songs', methods=['GET'])
@swag_from(song_get_all)
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

@song_bp.route('/songs', methods=['POST'])
@swag_from(song_create)
def create_song():
    data = request.get_json()
    artist = Artist.query.get(data['artist_id'])
    if not artist:
        return jsonify({'message': 'Artist not found'}), 404

    new_song = Song(
        title=data['title'],
        genre=data.get('genre', ''),
        artist_id=artist.id,
    )
    db.session.add(new_song)
    db.session.commit()
    return jsonify({'message': 'Song created successfully'}), 201

@song_bp.route('/playlists/<int:id>/songs', methods=['POST'])
@swag_from(add_song_to_playlist)
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

@song_bp.route('/playlists/<int:playlist_id>/songs/<int:song_id>', methods=['DELETE'])
@swag_from(remove_song_from_playlist)
def remove_song_from_playlist(playlist_id, song_id):
    entry = PlaylistSong.query.filter_by(
        playlist_id=playlist_id, song_id=song_id
    ).first_or_404()
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Song removed from playlist'}), 200

@song_bp.route('/songs/<int:artist_id>/artist', methods=['GET'])
@swag_from(songs_by_artist)
def get_songs_by_artist(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    songs = Song.query.filter_by(artist_id=artist.id).all()

    result = [
        {
            'id': song.id,
            'title': song.title,
            'genre': song.genre,
            'artist': artist.name,
        }
        for song in songs
    ]
    
    return jsonify(result), 200

@song_bp.route('/songs/genre/<string:genre>', methods=['GET'])
@swag_from(songs_by_genre)
def get_songs_by_genre(genre):
    sql_query = text("""
    SELECT song.id, song.title, song.genre
    FROM song
    WHERE song.genre = :genre
    """)
    result = db.session.execute(sql_query, {'genre': genre})
    rows = result.mappings().all()

    songs = [
        {
            'id': row['id'],
            'title': row['title'],
            'genre': row['genre'],
        }
        for row in rows
    ]
    
    return jsonify(songs), 200
