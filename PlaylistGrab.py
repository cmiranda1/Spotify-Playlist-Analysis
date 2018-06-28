import spotipy
import spotipy.oauth2 as oauth2
import json
import re
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import pyplot
from scipy import stats
import seaborn as sns
sns.set(color_codes=True)

#Create Login Token and Retrieve Playlist Info
#----------------------------------------------------------------------------------------------------------------------
client_id = 'YourClientID'
client_secret = 'YourClientSecret'
credentials = oauth2.SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

playlist_uri = 'PlaylistURI'
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

#Organize song information for playlist and download as CSV
#----------------------------------------------------------------------------------------------------------------------

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
    acousticness.append((re.findall("-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?", g[6]))[0])
    instrumentalness.append((re.findall("\d+", g[7]))[0])
    liveness.append((re.findall("\d+\.\d+", g[8]))[0])
    valence.append((re.findall("\d+\.\d+", g[9]))[0])
    tempo.append((re.findall("\d+\.\d+", g[10]))[0])


#Transform information into floats
#----------------------------------------------------------------------------------------------------------------------

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
mymatrix.to_csv("YourPlaylistName.csv")


#Plot Playlist attributes
#----------------------------------------------------------------------------------------------------------------------

fig = pyplot.figure()
ax = Axes3D(fig)
ax.scatter(speechiness,energy,valence)
pyplot.title("How Wordy, Energetic, and Positive is my Playlist?")
ax.set_xlabel("Speechiness")
ax.set_ylabel("Energy")
ax.set_zlabel("Valence")
pyplot.show()


f, axes = plt.subplots(2, 5, figsize=(4, 4),sharex=False,sharey=False)
sns.despine(left=True)
sns.distplot(danceability,label="Danceability",color='red', kde=False,fit=stats.gamma,ax=axes[0,0])
sns.distplot(energy,label="Energy", color='yellow',kde=False,fit=stats.gamma,ax=axes[0,1])
sns.distplot(key,label="Key",color='green',kde=False,fit=stats.gamma,ax=axes[0,2])
sns.distplot(loudness,label="Loudness",color='orange', kde=False,fit=stats.gamma,ax=axes[0,3])
sns.distplot(speechiness,label="Speechiness",color='magenta', kde=False,fit=stats.gamma,ax=axes[0,4])
sns.distplot(acousticness,label="Acousticness",color='cyan',kde=False,fit=stats.gamma,ax=axes[1,0])
sns.distplot(instrumentalness,label="Instrumentalness",color='pink', kde=False,fit=stats.gamma,ax=axes[1,1])
sns.distplot(liveness,label="Liveness",color='gray', kde=False,fit=stats.gamma,ax=axes[1,2])
sns.distplot(valence,label="Valence",color='blue',kde=False,fit=stats.gamma,ax=axes[1,3])
sns.distplot(tempo,label="Tempo",color='brown',kde=False,fit=stats.gamma,ax=axes[1,4])
pyplot.setp(axes, yticks=[])
axes[0,0].legend()
axes[0,1].legend()
axes[0,2].legend()
axes[0,3].legend()
axes[0,4].legend()
axes[1,0].legend()
axes[1,1].legend()
axes[1,2].legend()
axes[1,3].legend()
axes[1,4].legend()

pyplot.tight_layout()
pyplot.show()
