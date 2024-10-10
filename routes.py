from app import app
from flask import jsonify

# Get all playlists
@app.route('/playlists', methods=['GET'])
def get_playlists():
    result = []
    return jsonify(result), 200
