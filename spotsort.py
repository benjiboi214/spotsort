import click
import spotify
from tabulate import tabulate


class SpotSort:

    def __init__(self, spotify_client):
        self.spotify_client = spotify_client
        self.user_profile = self.spotify_client.get_user_profile()

    def __

    def parse_string_list(self, string):
        parsed = [x.strip() for x in string.split(',')]
        for selection in parsed:
            if selection not in valid_values:
                raise click.BadParameter(f"Selected an invalid playlist: {selection}", param=string)
        return

    def get_playlist_selection(self, playlists):
        # Prepare the data for printing with
        headers = ['ID', 'Name', 'Tracks', 'PID']
        tabular = [[i, x['name'], x['tracks']['total'], x['id']] for i,x in enumerate(playlists) if x['tracks']['total'] > 0]

        print("Available Playlists")
        print(tabulate(tabular, headers=headers))
        print('Select the playlists to add to the session.')
        value = click.prompt('Enter the playlists, using commas to separate the IDs', value_proc=self.parse_string_list)
        
        test_string = '1,5,7,10,20,40,42,58'
        test = self.parse_string_list(test_string, [x[0] for x in tabular])
    
        # selected = []
        # print("Entry was: ", value)
        # for entry in value:
        #     selected.append(int(entry) - 1)
        
        # headers = ['Name', 'Tracks']
        # tabular = []
        # for select in selected:
        #     tabular.append([playlists[select]['name'], playlists[select]['tracks']['total'] ])

        # print("Selected Playlists")
        # print(tabulate(tabular, headers=headers))


@click.command()
@click.argument('username')
def main(username):
    spotsort = SpotSort(spotify_client = spotify.Spotify(username))
    spotsort.user_playlists = spotsort.spotify_client.get_playlists(spotsort.user_profile['id'])

    spotsort.get_playlist_selection(spotsort.user_playlists)

if __name__ == '__main__':
    main()