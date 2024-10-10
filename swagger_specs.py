# swagger_specs.py

# Swagger specs for getting all playlists
playlist_get_all = {
    'operationId': 'getAllPlaylists',
    'summary': 'Get all playlists',
    'tags': ['Playlists'],
    'responses': {
        200: {
            'description': 'A list of all playlists',
            'schema': {
                'type': 'array',
                'items': {
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'description': {'type': 'string'}
                    }
                }
            }
        }
    }
}

# Swagger specs for creating a new playlist
playlist_create = {
    'operationId': 'createPlaylist',
    'summary': 'Create a new playlist',
    'tags': ['Playlists'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'name': {'type': 'string'},
                    'description': {'type': 'string'}
                },
                'required': ['name']
            }
        }
    ],
    'responses': {
        201: {'description': 'Playlist created successfully'},
        400: {'description': 'Invalid input'}
    }
}

# Swagger specs for getting a specific playlist by ID
playlist_get_by_id = {
    'operationId': 'getPlaylistById',
    'summary': 'Get a specific playlist by ID',
    'tags': ['Playlists'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the playlist to retrieve'
        }
    ],
    'responses': {
        200: {
            'description': 'Details of the playlist',
            'schema': {
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'description': {'type': 'string'},
                    'songs': {
                        'type': 'array',
                        'items': {
                            'properties': {
                                'id': {'type': 'integer'},
                                'title': {'type': 'string'},
                                'genre': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        },
        404: {'description': 'Playlist not found'}
    }
}

# Swagger specs for deleting a playlist
playlist_delete = {
    'operationId': 'deletePlaylist',
    'summary': 'Delete a playlist',
    'tags': ['Playlists'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the playlist to delete'
        }
    ],
    'responses': {
        200: {'description': 'Playlist deleted successfully'},
        404: {'description': 'Playlist not found'}
    }
}

# Swagger specs for getting all songs
song_get_all = {
    'operationId': 'getAllSongs',
    'summary': 'Get all songs',
    'tags': ['Songs'],
    'responses': {
        200: {
            'description': 'A list of all songs',
            'schema': {
                'type': 'array',
                'items': {
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'genre': {'type': 'string'}
                    }
                }
            }
        }
    }
}

# Swagger specs for creating a new song
song_create = {
    'operationId': 'createSong',
    'summary': 'Create a new song',
    'tags': ['Songs'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'title': {'type': 'string'},
                    'genre': {'type': 'string'}
                },
                'required': ['title']
            }
        }
    ],
    'responses': {
        201: {'description': 'Song created successfully'},
        400: {'description': 'Invalid input'}
    }
}

# Swagger specs for adding a song to a playlist
add_song_to_playlist = {
    'operationId': 'addSongToPlaylist',
    'summary': 'Add a song to a playlist',
    'tags': ['Playlists', 'Songs'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Playlist ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'song_id': {'type': 'integer'}
                },
                'required': ['song_id']
            }
        }
    ],
    'responses': {
        201: {'description': 'Song added to playlist'},
        400: {'description': 'Song already in playlist or invalid input'}
    }
}

# Swagger specs for removing a song from a playlist
remove_song_from_playlist = {
    'operationId': 'removeSongFromPlaylist',
    'summary': 'Remove a song from a playlist',
    'tags': ['Playlists', 'Songs'],
    'parameters': [
        {
            'name': 'playlist_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Playlist ID'
        },
        {
            'name': 'song_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Song ID'
        }
    ],
    'responses': {
        200: {'description': 'Song removed from playlist'},
        404: {'description': 'Entry not found'}
    }
}

# Swagger specs for getting playlists by genre
playlists_by_genre = {
    'operationId': 'getPlaylistsByGenre',
    'summary': 'Get playlists by song genre',
    'tags': ['Playlists'],
    'parameters': [
        {
            'name': 'genre',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'Genre of songs in the playlists'
        }
    ],
    'responses': {
        200: {
            'description': 'Playlists containing songs of the specified genre',
            'schema': {
                'type': 'array',
                'items': {
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'description': {'type': 'string'}
                    }
                }
            }
        }
    }
}
