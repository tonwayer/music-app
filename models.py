from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256))
    songs = db.relationship("PlaylistSong", back_populates="playlist")


class Song(db.Model):
    """Song model."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    genre = db.Column(db.String(64))
    playlists = db.relationship("PlaylistSong", back_populates="song")
    artist_id = db.Column(
        db.Integer, db.ForeignKey("artist.id", name="fk_song_artist"), nullable=True
    )


class PlaylistSong(db.Model):
    """Association table for Playlist and Song."""

    playlist_id = db.Column(db.Integer, db.ForeignKey("playlist.id"), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("song.id"), primary_key=True)
    playlist = db.relationship("Playlist", back_populates="songs")
    song = db.relationship("Song", back_populates="playlists")


class Artist(db.Model):
    """Artist model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    songs = db.relationship("Song", backref="artist", lazy=True)
