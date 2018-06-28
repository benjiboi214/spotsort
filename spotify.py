import os
from json.decoder import JSONDecodeError

import spotipy
import spotipy.util as util

import settings


class Spotify:

    def __init__(self, username):
        try:
            self.token = self.__create_token(username, settings.SPOTIFY_CLIENT_ID,
                settings.SPOTIFY_CLIENT_SECRET, settings.SPOTIFY_REDIRECT_URI)
        except (AttributeError, JSONDecodeError):
            os.remove(f".cache-{username}")
            self.token = self.__create_token(username, settings.SPOTIFY_CLIENT_ID,
                settings.SPOTIFY_CLIENT_SECRET, settings.SPOTIFY_REDIRECT_URI)
        self.client = spotipy.Spotify(auth=self.token)

    def __create_token(self, username, client_id, client_secret, redirect_uri):
        return util.prompt_for_user_token(
            username,
            'user-read-currently-playing user-read-playback-state',
            client_id=settings.SPOTIFY_CLIENT_ID,
            client_secret=settings.SPOTIFY_CLIENT_SECRET,
            redirect_uri=settings.SPOTIFY_REDIRECT_URI)

    def __handle_pagination(self, func):
        results = func
        items = results['items']
        while results['next']:
            results = self.client.next(results)
            items.extend(results['items'])
        return items

    def get_user_profile(self):
        return self.client.me()

    def get_playlists(self, user_id):
        return self.__handle_pagination(self.client.user_playlists(user_id))
    
    def get_current_song(self):
        return self.client.current_playback()
