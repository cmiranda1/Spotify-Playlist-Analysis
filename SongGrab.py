__author__ = 'colin_000'

import spotipy
import spotipy.oauth2 as oauth2
import json
import re
import seaborn as sns
sns.set(color_codes=True)

client_id = 'YourClientID'
client_secret = 'YourClientSecret'
credentials = oauth2.SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)


song_uri = 'spotify:track:6AzodcPEJtRce4f9aQeA1Z' #Jams

track_id = str(song_uri.split(':')[2])
#song = sp.audio_features(tracks='7foypmc7KZyU716Yv63BPe')
song = sp.audio_features(tracks=str(track_id))

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

song = json.dumps(song,indent=None)
song = song.split(",")
danceability.append((re.findall("\d+\.\d+", song[0]))[0])
energy.append((re.findall("\d+\.\d+", song[1]))[0])
key.append((re.findall("\d+", song[2]))[0])
loudness.append((re.findall("\d+\.\d+", song[3]))[0])
mode.append((re.findall("\d+", song[4]))[0])
speechiness.append((re.findall("\d+\.\d+", song[5]))[0])
acousticness.append((re.findall("-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?", song[6]))[0])
instrumentalness.append((re.findall("\d+", song[7]))[0])
liveness.append((re.findall("\d+\.\d+", song[8]))[0])
valence.append((re.findall("\d+\.\d+", song[9]))[0])
tempo.append((re.findall("\d+\.\d+", song[10]))[0])

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

print([speechiness[0],energy[0],valence[0],danceability[0],key[0],loudness[0],mode[0],acousticness[0],instrumentalness[0],liveness[0],tempo[0]])