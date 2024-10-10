# swagger_specs.py

# Swagger specs for getting all playlists
playlist_get_all = {
    "operationId": "getAllPlaylists",
    "summary": "Get all playlists",
    "tags": ["Playlists"],
    "responses": {
        200: {
            "description": "A list of all playlists",
            "schema": {
                "type": "array",
                "items": {
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                    }
                },
            },
        }
    },
}

# Swagger specs for creating a new playlist
playlist_create = {
    "operationId": "createPlaylist",
    "summary": "Create a new playlist",
    "tags": ["Playlists"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                },
                "required": ["name"],
            },
        }
    ],
    "responses": {
        201: {"description": "Playlist created successfully"},
        400: {"description": "Invalid input"},
    },
}

# Swagger specs for getting a specific playlist by ID
playlist_get_by_id = {
    "operationId": "getPlaylistById",
    "summary": "Get a specific playlist by ID",
    "tags": ["Playlists"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID of the playlist to retrieve",
        }
    ],
    "responses": {
        200: {
            "description": "Details of the playlist",
            "schema": {
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "songs": {
                        "type": "array",
                        "items": {
                            "properties": {
                                "id": {"type": "integer"},
                                "title": {"type": "string"},
                                "genre": {"type": "string"},
                            }
                        },
                    },
                }
            },
        },
        404: {"description": "Playlist not found"},
    },
}

# Swagger specs for deleting a playlist
playlist_delete = {
    "operationId": "deletePlaylist",
    "summary": "Delete a playlist",
    "tags": ["Playlists"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID of the playlist to delete",
        }
    ],
    "responses": {
        200: {"description": "Playlist deleted successfully"},
        404: {"description": "Playlist not found"},
    },
}

# Swagger specs for getting all songs
song_get_all = {
    "operationId": "getAllSongs",
    "summary": "Get all songs",
    "tags": ["Songs"],
    "responses": {
        200: {
            "description": "A list of all songs",
            "schema": {
                "type": "array",
                "items": {
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "genre": {"type": "string"},
                    }
                },
            },
        }
    },
}

# Swagger specs for creating a new song
song_create = {
    "operationId": "createSong",
    "summary": "Create a new song",
    "tags": ["Songs"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "properties": {
                    "title": {"type": "string"},
                    "genre": {"type": "string"},
                    "artist_id": {"type": "integer"},
                },
                "required": ["title"],
            },
        }
    ],
    "responses": {
        201: {"description": "Song created successfully"},
        400: {"description": "Invalid input"},
    },
}

# Swagger specs for adding a song to a playlist
add_song_to_playlist = {
    "operationId": "addSongToPlaylist",
    "summary": "Add a song to a playlist",
    "tags": ["Links"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "Playlist ID",
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "properties": {"song_id": {"type": "integer"}},
                "required": ["song_id"],
            },
        },
    ],
    "responses": {
        201: {"description": "Song added to playlist"},
        400: {"description": "Song already in playlist or invalid input"},
    },
}

# Swagger specs for removing a song from a playlist
remove_song_from_playlist = {
    "operationId": "removeSongFromPlaylist",
    "summary": "Remove a song from a playlist",
    "tags": ["Links"],
    "parameters": [
        {
            "name": "playlist_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "Playlist ID",
        },
        {
            "name": "song_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "Song ID",
        },
    ],
    "responses": {
        200: {"description": "Song removed from playlist"},
        404: {"description": "Entry not found"},
    },
}

# Swagger specs for getting playlists by genre
playlists_by_genre = {
    "operationId": "getPlaylistsByGenre",
    "summary": "Get playlists by song genre",
    "tags": ["Group"],
    "parameters": [
        {
            "name": "genre",
            "in": "path",
            "type": "string",
            "required": True,
            "description": "Genre of songs in the playlists",
        }
    ],
    "responses": {
        200: {
            "description": "Playlists containing songs of the specified genre",
            "schema": {
                "type": "array",
                "items": {
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                    }
                },
            },
        }
    },
}

# Swagger specs for getting all artists
artist_get_all = {
    "operationId": "getAllArtists",
    "summary": "Get all artists",
    "tags": ["Artists"],
    "responses": {
        200: {
            "description": "A list of all artists",
            "schema": {
                "type": "array",
                "items": {
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                    }
                },
            },
        }
    },
}

# Swagger specs for creating a new artist
artist_create = {
    "operationId": "createArtist",
    "summary": "Create a new artist",
    "tags": ["Artists"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        }
    ],
    "responses": {
        201: {"description": "Artist created successfully"},
        400: {"description": "Invalid input"},
    },
}

# Swagger specs for getting a specific artist by ID
artist_get_by_id = {
    "operationId": "getArtistById",
    "summary": "Get a specific artist by ID",
    "tags": ["Artists"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID of the artist to retrieve",
        }
    ],
    "responses": {
        200: {
            "description": "Details of the artist",
            "schema": {
                "properties": {"id": {"type": "integer"}, "name": {"type": "string"}}
            },
        },
        404: {"description": "Artist not found"},
    },
}

# Swagger specs for updating an artist
artist_update = {
    "operationId": "updateArtist",
    "summary": "Update an existing artist",
    "tags": ["Artists"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID of the artist to update",
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        },
    ],
    "responses": {
        200: {"description": "Artist updated successfully"},
        400: {"description": "Invalid input"},
        404: {"description": "Artist not found"},
    },
}

# Swagger specs for deleting an artist
artist_delete = {
    "operationId": "deleteArtist",
    "summary": "Delete an artist",
    "tags": ["Artists"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID of the artist to delete",
        }
    ],
    "responses": {
        200: {"description": "Artist deleted successfully"},
        404: {"description": "Artist not found"},
    },
}

# Swagger specs for getting songs by a specific artist
songs_by_artist = {
    "operationId": "getSongsByArtist",
    "summary": "Get all songs by a specific artist",
    "tags": ["Group"],
    "parameters": [
        {
            "name": "artist_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID of the artist to retrieve songs for",
        }
    ],
    "responses": {
        200: {
            "description": "Songs for the specified artist",
            "schema": {
                "type": "array",
                "items": {
                    "properties": {
                        "id": {"type": "integer"},
                        "title": {"type": "string"},
                        "genre": {"type": "string"},
                        "artist": {"type": "string"},
                    }
                },
            },
        },
        404: {"description": "Artist not found"},
    },
}

# Swagger specs for getting songs by genre using raw SQL
songs_by_genre = {
    "operationId": "getSongsByGenre",
    "summary": "Get all songs by genre using raw SQL",
    "tags": ["Group"],
    "parameters": [
        {
            "name": "genre",
            "in": "path",
            "type": "string",
            "required": True,
            "description": "Genre of the songs to retrieve",
        }
    ],
    "responses": {
        200: {
            "description": "Songs for the specified genre",
            "schema": {
                "type": "array",
                "items": {
                    "properties": {
                        "id": {"type": "integer"},
                        "title": {"type": "string"},
                        "genre": {"type": "string"},
                    }
                },
            },
        },
        404: {"description": "No songs found for the specified genre"},
    },
}
