# Music Library API

## Overview

The **Music Library API** is a RESTful service that allows users to manage playlists and songs in a digital music library.

## Technologies Used

- **Python 3.x**
- **Flask**: Web framework for building the API.
- **Flask_SQLAlchemy**: ORM for database interactions.
- **Flask_Migrate**: Handles database migrations.
- **Flasgger**: Integrates Swagger UI for API documentation.
- **SQLite**: Lightweight database for development and testing.

## Installation and Setup

### Prerequisites

- Python 3.x installed
- `pip` package manager

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tonwayer/music_app.git
   cd music_app
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Unix/MacOS
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**

   ```bash
   flask db upgrade
   ```

5. **Run the Application**

   ```bash
   flask run
   ```

   The application will be accessible at `http://localhost:5000`.

## API Documentation

Detailed API documentation is available via Swagger UI.

- **Access Swagger UI**: Navigate to `http://localhost:5000/apidocs/` in your web browser.

Swagger UI provides an interactive interface to explore and test all available endpoints, view request and response formats, and understand the API's capabilities.

## Key Features

- **Playlist Management**
  - Create, retrieve, update, and delete playlists.
  - Add or remove songs from playlists.

- **Song Management**
  - Create, retrieve, update, and delete songs.
  - Retrieve songs by genre and artist.

- **Artist Management**
  - Manage artist data.

## Database Schema

### Tables and Relationships

- **Artist**
  - `id` (Primary Key)
  - `name`
  - **Relationship**: One-to-Many with **Song**

- **Song**
  - `id` (Primary Key)
  - `title`
  - `genre`
  - `artist_id` (Foreign Key to `Artist.id`)
  - **Relationships**:
    - Many-to-One with **Artist**
    - Many-to-Many with **Playlist** via **PlaylistSong**

- **Playlist**
  - `id` (Primary Key)
  - `name`
  - `description`
  - **Relationship**: Many-to-Many with **Song** via **PlaylistSong**

- **PlaylistSong** (Association Table)

## Design Choices

- **Flask Blueprints**: Routes are organized using Blueprints for better modularity and maintainability.
- **SQLAlchemy ORM**: Used for database interactions, with explicit constraint names for better schema management.
- **Non-Trivial SQL Queries**: Implemented complex queries using raw SQL for advanced data retrieval, such as window functions for aggregations.
- **Swagger Documentation**: Provides an interactive UI for API exploration without cluttering the README with detailed endpoint information.
