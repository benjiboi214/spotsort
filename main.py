import click

import settings
from spotify import Spotify
from spotsort import SpotSort

@click.group()
@click.option('--username', default=settings.DEFAULT_USER, help='Username to authenticate as')
@click.pass_context
def cli(ctx, username):
    ctx.obj['username'] = username

@cli.command()
@click.pass_context
def current_song(ctx):
    ss = SpotSort(spotify_client = Spotify(ctx.obj['username']))
    ss.start_this_song_session()
    
@cli.command()
@click.pass_context
def playlist_sort(ctx):
    ss = SpotSort(spotify_client = Spotify(ctx.obj['username']))
    ss.start_playlist_sort_session()

if __name__ == '__main__':
    cli(obj={})
