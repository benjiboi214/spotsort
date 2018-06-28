import click

import settings
import spotify
import spotsort

@click.group()
@click.option('--username', default=settings.DEFAULT_USER, help='Username to authenticate as')
@click.pass_context
def cli(ctx, username):
    ctx.obj['username'] = username

@cli.command()
@click.pass_context
def current_song(ctx):
    ss = spotsort.SpotSort(spotify_client = spotify.Spotify(ctx.obj['username']))
    

@cli.command()
@click.pass_context
def playlist_sort(ctx):
    ss = spotsort.SpotSort(spotify_client = spotify.Spotify(ctx.obj['username']))
    ss.user_playlists = ss.spotify_client.get_playlists(ss.user_profile['id'])

    ss.get_playlist_selection(ss.user_playlists)

if __name__ == '__main__':
    cli(obj={})
