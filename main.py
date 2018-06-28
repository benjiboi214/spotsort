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
    ss = spotsort.SpotSort(spotify_client = spotify.Spotify(ctx.obj['username']))
    
@cli.command()
@click.pass_context
def playlist_sort(ctx):
    ss = SpotSort(spotify_client = Spotify(ctx.obj['username']))
    ss.start_playlist_sort_session()

@cli.command()
def test_django():
    # Django specific settings
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    # Ensure settings are read
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

    # Your application specific imports
    from data.models import User


    #Add user
    user = User(name="masnun", email="masnun@gmail.com")
    user.save()

    # Application logic
    first_user = User.objects.all()[0]

    print(first_user.name)
    print(first_user.email)
    ss = SpotSort(spotify_client = Spotify(ctx.obj['username']))
    ss.start_this_song_session()


if __name__ == '__main__':
    cli(obj={})
