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

if __name__ == '__main__':
    cli(obj={})
