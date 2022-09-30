import spotipy
from utils.config_reader import config
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=config["spotify_client_id"],
                                                      client_secret=config["spotify_secret_key"])
spotify_client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
