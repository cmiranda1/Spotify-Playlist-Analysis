__author__ = 'colin_000'

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

any = pd.read_csv('Anytime.csv')
anyspeech = any['speechiness'].values
anyenergy = any['energy'].values
anyvalen = any['valence'].values
anydance = any['danceability'].values
anykey = any['key'].values
anyloud = any['loudness'].values
anymode = any['mode'].values
anyacou = any['acousticness'].values
anyint = any['instrumentalness'].values
anyliv = any['liveness'].values
anytem = any['tempo'].values
anylab = []

for i in range(len(anyspeech)):
    anylab.append("Anytime")

anytime = pd.DataFrame({'speechiness':anyspeech,'energy':anyenergy,'valence':anyvalen,'danceability':anydance, 'key':anykey,'loudness':anyloud,'mode':anymode,'acousticness':anyacou,'instrumentalness':anyint,'liveness':anyliv,'tempo':anytem,'playlist':anylab})

jim = pd.read_csv('TheJimPlaylist.csv')
jimspeech = jim['speechiness'].values
jimenergy = jim['energy'].values
jimvalen = jim['valence'].values
jimdance = jim['danceability'].values
jimkey = jim['key'].values
jimloud = jim['loudness'].values
jimmode = jim['mode'].values
jimacou = jim['acousticness'].values
jimint = jim['instrumentalness'].values
jimliv = jim['liveness'].values
jimtem = jim['tempo'].values
jimlab = []

for i in range(len(jimspeech)):
    jimlab.append("Gym")

jimlist = pd.DataFrame({'speechiness':jimspeech,'energy':jimenergy,'valence':jimvalen,'danceability':jimdance, 'key':jimkey,'loudness':jimloud,'mode':jimmode,'acousticness':jimacou,'instrumentalness':jimint,'liveness':jimliv,'tempo':jimtem,'playlist':jimlab})


book= pd.read_csv('Jams.csv')
bookspeech = book['speechiness'].values
bookenergy = book['energy'].values
bookvalen = book['valence'].values
bookdance = book['danceability'].values
bookkey = book['key'].values
bookloud = book['loudness'].values
bookmode = book['mode'].values
bookacou = book['acousticness'].values
bookint = book['instrumentalness'].values
bookliv = book['liveness'].values
booktem = book['tempo'].values
booklab = []

for i in range(len(bookspeech)):
    booklab.append("Jams")

books = pd.DataFrame({'speechiness':bookspeech,'energy':bookenergy,'valence':bookvalen,'danceability':bookdance, 'key':bookkey,'loudness':bookloud,'mode':bookmode,'acousticness':bookacou,'instrumentalness':bookint,'liveness':bookliv,'tempo':booktem,'playlist':booklab})


frame = [anytime,jimlist,books]
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


ax1 = Axes3D(plt.figure())
ax1.scatter(anyspeech,anyenergy,anyvalen,alpha=.6,color='r')
ax1.scatter(jimspeech,jimenergy,jimvalen,alpha=.6,color='b')
ax1.scatter(bookspeech,bookenergy,bookvalen,alpha=.6,color='g')

plt.show()

X_train = []
Y_train = []

for i in range(len(speechiness)):

    X_train.append([speechiness[i],energy[i],valence[i],danceability[i],key[i],loudness[i],mode[i],acousticness[i],instrumentalness[i],liveness[i],tempo[i]])
    Y_train.append([playlist[i]])

model = KNeighborsClassifier(n_neighbors=7)
model.fit(X_train,Y_train)

song = [0.0891, 0.816, 0.22, 0.731, 11.0, 5.595, 1.0, 0.467, 0.0, 0.189, 109.943]

x = model.predict([song])
y = model.predict_proba([song])
print(x)
print(y)

