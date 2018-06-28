import click
from tabulate import tabulate


class SpotSort:
    presented_to_user = []
    selected_playlists = []

    def __init__(self, spotify_client):
        self.spotify_client = spotify_client
        self.user_profile = self.spotify_client.get_user_profile()

    def __print_tabulated_data(self, pre_string,post_string, tabulated_data, tabulated_headers):
        self.present_to_user = tabulated_data
        print(pre_string)
        print(tabulate(tabulated_data, headers=tabulated_headers))
        print(post_string)
        return

    def __parse_string_list(self, string):
        parsed = [int(x.strip()) for x in string.split(',')]
        valid = [x[0] for x in self.present_to_user]
        for selection in parsed:
            if selection not in valid:
                raise click.BadParameter(f"Selected an invalid playlist: {selection}", param=string)
        return parsed

    def __get_playlist_selection(self, playlists):
        # Prepare the data for printing with tabulate
        playlists_to_present_headers = ['ID', 'Name', 'Tracks', 'PID']
        playlists_to_present = [[i, x['name'], x['tracks']['total'], x['id']] for i,x in enumerate(playlists) if x['tracks']['total'] > 0]

        self.__print_tabulated_data(
            'Available Playlists',
            'Select the playlists to add to the session.',
            playlists_to_present,
            playlists_to_present_headers)
        selected_indexes = click.prompt('Enter the playlists, using commas to separate the IDs', value_proc=self.__parse_string_list)
    
        return [playlists[x] for x in selected_indexes]
    
    def start_playlist_sort_session(self):
        self.user_profile = self.spotify_client.get_user_profile()
        self.user_playlists = self.spotify_client.get_playlists(self.user_profile['id'])
        songs = self.__get_playlist_selection(self.user_playlists)
        for song in songs:
            # Listener Class
            pass
        return


    def start_this_song_session(self):
        current = self.spotify_client.get_current_song()
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(current)
        # print(current)
        pass


class Listen:
    pass

    # manage time state
    # manage start playing
    # manage stop playing
    # manage collecting input for seeking

    # Controls
    ## Seek through song  - 1/8ths(?) through song per input using ms (seek_track(position_ms, device_id=None))
    ## Categorise - Move down into the categorisation module
    ## Pause - Pause Current Song (pause_playback(device_id=None))
    ## Play - Resume Current Song (start_playback(device_id=None, context_uri=None, uris=None, offset=None))
    ## Start Over - Seek to start of current song (seek_track(position_ms, device_id=None))
    ## Skip - Move up to calling module with skip signal


# Architecture
## Entry points

# Start Playlist Session
#  - Select playlists to sort
#  - Determine how sorting will work
#  - Harvest Song URIs from playlists
#  - For Each Song
#  - - Play song
#  - - Provide interface to control song
#  - - Categorise Song
#  - - Write Categories to data structure

# I like this Song!
# - Capture current song
# - provide interface to control song
# - categorise song
# - Write Categories to data structure

## Data Model
# Song
# - Genre 
# - - Many genres to one song
# - Sub Genre
# - - Many sub genres to one song
# - Energy
# - - One Energy to One Song
# - Environment
# - - Where would I play it?
# - - Where does it suit?
# - Elements
# - - Bass
# - - Pace
# - - Vocals

## Class Model
# - Entry class
# - - Has a start session method
# - - - Select Playlist method
# - - - Populate List of Songs to Sort
# - - - Enter Song listening mode
# - - Has a capture song method
# - - - Get the currently playing song
# - - - Enter Song listening mode

# - Listener
# - - Single entry point (public method)
# - - Determine if song is already playing
# - - Determine if song is already in DB
# - - - Present current details if yes
# - - Present Controls (loop)
# - - -  ## Seek through song  - 1/8ths(?) through song per input using ms (seek_track(position_ms, device_id=None))
# - - -  ## Categorise - Move down into the categorisation module
# - - -  ## Pause - Pause Current Song (pause_playback(device_id=None))
# - - -  ## Play - Resume Current Song (start_playback(device_id=None, context_uri=None, uris=None, offset=None))
# - - -  ## Start Over - Seek to start of current song (seek_track(position_ms, device_id=None))
# - - -  ## Skip - Move up to calling module with skip signal

# - Categorise
# - - Present Genres
# - - Present Sub Genres
# - - Present Energy
# - - Present Environment
# - - Present Each element
# - For each, present exiasting options, or create new option