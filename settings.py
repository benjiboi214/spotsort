# settings.py
import os
from dotenv import load_dotenv
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
SPOTIFY_REQUIRED_API_SCOPES = [
    'user-modify-playback-state',  # To enable the playing/pausing/skipping through songs
    'playlist-read-private'  # To get the full list of available playlists to navigate through.
]
