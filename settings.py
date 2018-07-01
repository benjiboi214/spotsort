# settings.py
import os
from dotenv import load_dotenv
load_dotenv()

# Spotify App Developer Details
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = 'http://localhost:8888/callback'
SPOTIFY_REQUIRED_API_SCOPES = [
    'user-modify-playback-state',  # To enable the playing/pausing/skipping through songs
    'playlist-read-private'  # To get the full list of available playlists to navigate through.
]

# Default Spotify User if not specified on CLI
DEFAULT_USER = 'benjiboi214'


## Djangpo ORM Settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!ll2kn4tq9+xyz&ahyy(v_5ag0p#dptvbt1#p6fsw177n$+_0s'

INSTALLED_APPS = [
    'data'
]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}