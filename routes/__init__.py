from flask import Flask
from .playlists import playlist_bp
from .songs import song_bp

def register_blueprints(app: Flask):
    """Function to register blueprints to the main app"""
    app.register_blueprint(playlist_bp)
    app.register_blueprint(song_bp)
