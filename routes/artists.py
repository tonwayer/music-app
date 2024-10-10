from models import db
from flask import Blueprint, jsonify, request
from models import Artist
from flasgger.utils import swag_from
from swagger_specs import (
    artist_get_all,
    artist_create,
    artist_get_by_id,
    artist_update,
    artist_delete,
)

# Define Blueprint
artist_bp = Blueprint("artists", __name__)


# Get all artists
@artist_bp.route("/artists", methods=["GET"])
@swag_from(artist_get_all)
def get_artists():
    artists = Artist.query.all()
    result = [{"id": artist.id, "name": artist.name} for artist in artists]
    return jsonify(result), 200


# Create a new artist
@artist_bp.route("/artists", methods=["POST"])
@swag_from(artist_create)
def create_artist():
    data = request.get_json()
    new_artist = Artist(name=data["name"])
    db.session.add(new_artist)
    db.session.commit()
    return jsonify({"message": "Artist created successfully"}), 201


# Get a specific artist by ID
@artist_bp.route("/artists/<int:id>", methods=["GET"])
@swag_from(artist_get_by_id)
def get_artist(id):
    artist = Artist.query.get_or_404(id)
    result = {"id": artist.id, "name": artist.name}
    return jsonify(result), 200


# Update an existing artist
@artist_bp.route("/artists/<int:id>", methods=["PUT"])
@swag_from(artist_update)
def update_artist(id):
    artist = Artist.query.get_or_404(id)
    data = request.get_json()
    artist.name = data.get("name", artist.name)  # Update the artist's name if provided
    db.session.commit()
    return jsonify({"message": "Artist updated successfully"}), 200


# Delete an artist
@artist_bp.route("/artists/<int:id>", methods=["DELETE"])
@swag_from(artist_delete)
def delete_artist(id):
    artist = Artist.query.get_or_404(id)
    db.session.delete(artist)
    db.session.commit()
    return jsonify({"message": "Artist deleted successfully"}), 200
