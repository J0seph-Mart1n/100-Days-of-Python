import os

from bs4 import BeautifulSoup
import requests
# import pprint
#Extracting songs of Top 100 Billboard from a specific date
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
billboard_website = response.text

soup = BeautifulSoup(billboard_website, "html.parser")

top_songs = soup.select(selector="li ul li h3")
top_songs_name = [songs.get_text().strip() for songs in top_songs]
# print(top_songs_name)
# print(len(top_songs_name))

import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()["id"]
year = date.split("-")[0]
song_uris = []
for song in top_songs_name:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    # pprint.pp(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on spotify.")

user_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=True, description="Playlist created using python")
playlist_id = user_playlist['id']
create_playlist = sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
print(create_playlist)