__author__ = 'colin_000'

import spotipy
import spotipy.oauth2 as oauth2
import json
import re
import pandas as pd
import seaborn as sns

sns.set(color_codes=True)

client_id = 'YourClientID'
client_secret = 'YourClientSecret'
credentials = oauth2.SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

playlist_uri = 'PlaylistURI' #Playlist URI can be retrieved from the "Share" tab on Spotify

username = playlist_uri.split(':')[2]
playlist = playlist_uri.split(':')[4]
tracks = []
tracks = sp.user_playlist(username, playlist,fields='tracks,next')
results = json.dumps(tracks,indent=None)
results = results.split('"uri": "spotify:track:')
results.pop(0)
trackids = []
for i in results:
    x = i[:22]
    trackids.append(x)


attributes = []
for y in trackids:
    at1 = sp.audio_features(tracks=y)
    attributes.append(at1)

danceability = []
energy = []
key = []
loudness = []
mode = []
speechiness = []
acousticness = []
instrumentalness = []
liveness = []
valence = []
tempo = []


for g in attributes:
    g = json.dumps(g,indent=None)
    g = g.split(",")
    danceability.append((re.findall("\d+\.\d+", g[0]))[0])
    energy.append((re.findall("\d+\.\d+", g[1]))[0])
    key.append((re.findall("\d+", g[2]))[0])
    loudness.append((re.findall("\d+\.\d+", g[3]))[0])
    mode.append((re.findall("\d+", g[4]))[0])
    speechiness.append((re.findall("\d+\.\d+", g[5]))[0])
    #acousticness.append((re.findall("\d+\.\d+", g[6]))[0])
    acousticness.append((re.findall("-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?", g[6]))[0])
    instrumentalness.append((re.findall("\d+", g[7]))[0])
    liveness.append((re.findall("\d+\.\d+", g[8]))[0])
    valence.append((re.findall("\d+\.\d+", g[9]))[0])
    tempo.append((re.findall("\d+\.\d+", g[10]))[0])


danceability = [float(i) for i in danceability]
energy = [float(i) for i in energy]
key = [float(i) for i in key]
loudness = [float(i) for i in loudness]
mode = [float(i) for i in mode]
speechiness = [float(i) for i in speechiness]
acousticness = [float(i) for i in acousticness]
instrumentalness = [float(i) for i in instrumentalness]
liveness = [float(i) for i in liveness]
valence = [float(i) for i in valence]
tempo = [float(i) for i in tempo]

mymatrix = pd.DataFrame({'danceability':danceability,'energy':energy,'key':key,'loudness':loudness,'mode':mode,'speechiness':speechiness,'acousticness':acousticness,'instrumentalness':instrumentalness,'liveness':liveness,'valence':valence,'tempo':tempo})
mymatrix.to_csv("PlaylistTitle.csv")

