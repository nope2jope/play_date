import os
import spotipy
from spotipy import oauth2


CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = 'http://google.com/'
SCOPE = 'playlist-modify-public'

def lovely_gesture(song_list):

    play_name = input("What would you like to call this playlist? ")
    cache = f'.spotipy.{play_name}'
    oauth_token = oauth2.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET,REDIRECT_URI,scope=SCOPE, cache_path=cache)
    spotify = spotipy.Spotify(auth_manager=oauth_token)
    user = spotify.current_user()['id']
    new_playlist = spotify.user_playlist_create(user=user, name=play_name)
    uri_list = []

    for song in song_list:
        track_name = song['track']
        searched_track = spotify.search(q=f'{track_name}', type='track', limit=1)
        track_uri = searched_track['tracks']['items'][0]['id']
        uri_list.append(track_uri)

    if new_playlist:
        play_id = new_playlist['id']
        spotify.playlist_add_items(playlist_id=play_id, items=uri_list)


