from utils.spotipy_manipulator import spotify_client

s = spotify_client.search(q='Tool', type='artist', limit=3)

print(s)
