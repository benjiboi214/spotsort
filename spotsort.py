import click
import spotify
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
        print(parsed)
        valid = [x[0] for x in self.present_to_user]
        print(valid)
        for selection in parsed:
            if selection not in valid:
                raise click.BadParameter(f"Selected an invalid playlist: {selection}", param=string)
        return parsed

    def get_playlist_selection(self, playlists):
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


@click.command()
@click.argument('username')
def main(username):
    spotsort = SpotSort(spotify_client = spotify.Spotify(username))
    spotsort.user_playlists = spotsort.spotify_client.get_playlists(spotsort.user_profile['id'])

    spotsort.get_playlist_selection(spotsort.user_playlists)

if __name__ == '__main__':
    main()