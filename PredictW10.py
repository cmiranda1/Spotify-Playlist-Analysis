__author__ = 'colin_000'
import spotipy
import spotipy.oauth2 as oauth2
import json
import re
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import pyplot

#Loading and Transforming CSV files from PlaylistGrab into DataFrames
#----------------------------------------------------------------------------------------------------------------------


playlist1 = pd.read_csv('Playlist1.csv')
speech1 = playlist1['speechiness'].values
energy1 = playlist1['energy'].values
valence1 = playlist1['valence'].values
dance1 = playlist1['danceability'].values
key1 = playlist1['key'].values
loud1 = playlist1['loudness'].values
mode1 = playlist1['mode'].values
acoustic1 = playlist1['acousticness'].values
instrum1 = playlist1['instrumentalness'].values
live1 = playlist1['liveness'].values
tempo1 = playlist1['tempo'].values
lab1 = []

for i in range(len(speech1)):
    lab1.append("Playlist1")

list1 = pd.DataFrame({'speechiness':speech1,'energy':energy1,'valence':valence1,'danceability':dance1, 'key':key1,'loudness':loud1,'mode':mode1,'acousticness':acoustic1,'instrumentalness':instrum1,'liveness':live1,'tempo':tempo1,'playlist':lab1})

playlist2 = pd.read_csv('Playlist2.csv')
speech2 = playlist2['speechiness'].values
energy2 = playlist2['energy'].values
valence2 = playlist2['valence'].values
dance2 = playlist2['danceability'].values
key2 = playlist2['key'].values
loud2 = playlist2['loudness'].values
mode2 = playlist2['mode'].values
acoustic2 = playlist2['acousticness'].values
instrum2 = playlist2['instrumentalness'].values
live2 = playlist2['liveness'].values
tempo2 = playlist2['tempo'].values
lab2 = []

for i in range(len(speech2)):
    lab2.append("Playlist2")

list2 = pd.DataFrame({'speechiness':speech2,'energy':energy2,'valence':valence2,'danceability':dance2, 'key':key2,'loudness':loud2,'mode':mode2,'acousticness':acoustic2,'instrumentalness':instrum2,'liveness':live2,'tempo':tempo2,'playlist':lab2})


playlist3= pd.read_csv('Playlist3.csv')
speech3 = playlist3['speechiness'].values
energy3 = playlist3['energy'].values
valence3 = playlist3['valence'].values
dance3 = playlist3['danceability'].values
key3 = playlist3['key'].values
loud3 = playlist3['loudness'].values
mode3 = playlist3['mode'].values
acoustic3 = playlist3['acousticness'].values
instrum3 = playlist3['instrumentalness'].values
live3 = playlist3['liveness'].values
tempo3 = playlist3['tempo'].values
lab3 = []

for i in range(len(speech3)):
    lab3.append("Playlist3")

list3 = pd.DataFrame({'speechiness':speech3,'energy':energy3,'valence':valence3,'danceability':dance3, 'key':key3,'loudness':loud3,'mode':mode3,'acousticness':acoustic3,'instrumentalness':instrum3,'liveness':live3,'tempo':tempo3,'playlist':lab3})

#Combine DataFrames into a single called merged and separate columnts
#----------------------------------------------------------------------------------------------------------------------

frame = [list1,list2,list3]
merged = pd.concat(frame)

speechiness = merged['speechiness'].values
energy = merged['energy'].values
valence = merged['valence'].values
playlist = merged['playlist'].values
danceability = merged['danceability'].values
key = merged['key'].values
loudness = merged['loudness'].values
mode = merged['mode'].values
acousticness = merged['acousticness'].values
instrumentalness = merged['instrumentalness'].values
liveness = merged['liveness'].values
tempo = merged['tempo'].values


#Scatter plot of 3 most important attributes
#-----------------------------------------------------------------------------------------------------------------------
fig = pyplot.figure()
ax1 = Axes3D(fig)
ax1.scatter(speech1,energy1,valence1,color='r')
ax1.scatter(speech2,energy2,valence2,color='b')
ax1.scatter(speech3,energy3,valence3,color='g')
ax1.set_xlabel('Speechiness')
ax1.set_ylabel('Energy')
ax1.set_zlabel('Valence')
ax1.legend()

#s = sns.pairplot(merged,hue='playlist')
#g = (sns.jointplot(speechiness, valence).plot_joint(sns.kdeplot, zorder=0, n_levels=6))
#c = sns.jointplot(speechiness,valence,kind="kde", space=0, color="g")
plt.show()

#Train K Nearest Neighbor Models
#----------------------------------------------------------------------------------------------------------------------
X_train = []
Y_train = []

for i in range(len(speechiness)):
    #X_train.append([speechiness[i],energy[i],valence[i]])
    #X_train.append([speechiness[i],energy[i],valence[i],danceability[i]])
    X_train.append([speechiness[i],energy[i],valence[i],danceability[i],key[i],loudness[i],mode[i],acousticness[i],instrumentalness[i],liveness[i],tempo[i]])
    Y_train.append([playlist[i]])

model = KNeighborsClassifier(n_neighbors=7)
model.fit(X_train,Y_train)

#Grab song to place using song URI
#-----------------------------------------------------------------------------------------------------------------------

client_id = 'YourClientID'
client_secret = 'YourClientSecret'
credentials = oauth2.SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

song_uri = 'TrackURI'

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

song = [speechiness[0],energy[0],valence[0],danceability[0],key[0],loudness[0],mode[0],acousticness[0],instrumentalness[0],liveness[0],tempo[0]]


#Assess which playlist the song should belong to
#-----------------------------------------------------------------------------------------------------------------------

x = model.predict([song])
y = model.predict_proba([song])
print(x)
print(y)

