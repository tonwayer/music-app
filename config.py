import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Configuration for Flask application."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
