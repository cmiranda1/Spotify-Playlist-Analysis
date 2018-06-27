__author__ = 'colin_000'

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot
import seaborn as sns

any = pd.read_csv('Anytime.csv')
anyspeech = any['speechiness'].values
anyenergy = any['energy'].values
anyvalen = any['valence'].values
anylab = []

for i in range(len(anyspeech)):
    anylab.append("Anytime")

anytime = pd.DataFrame({'speechiness':anyspeech,'energy':anyenergy,'valence':anyvalen,'playlist':anylab})

jim = pd.read_csv('TheJimPlaylist.csv')
jimspeech = jim['speechiness'].values
jimenergy = jim['energy'].values
jimvalen = jim['valence'].values
jimlab = []

for i in range(len(jimspeech)):
    jimlab.append("Jim")

jimlist = pd.DataFrame({'speechiness':jimspeech,'energy':jimenergy,'valence':jimvalen,'playlist':jimlab})

book= pd.read_csv('Jams.csv')
bookspeech = book['speechiness'].values
bookenergy = book['energy'].values
bookvalen = book['valence'].values
booklab = []

for i in range(len(bookspeech)):
    booklab.append("Jams")

books= pd.DataFrame({'speechiness':bookspeech,'energy':bookenergy,'valence':bookvalen,'playlist':booklab})

frame = [anytime,jimlist,books]
merged = pd.concat(frame)

speechiness = merged['speechiness'].values
energy = merged['energy'].values
valence = merged['valence'].values
playlist = merged['playlist'].values

s = sns.pairplot(merged,hue='playlist')
pyplot.show()

X_train = []
Y_train = []

for i in range(len(speechiness)):
    X_train.append([speechiness[i],energy[i],valence[i]])
    Y_train.append([playlist[i]])

model = KNeighborsClassifier()
model.fit(X_train,Y_train)

x = model.predict([[0.588,0.642,0.0658]])
y = model.predict_proba([[0.088,0.642,0.0658]])
print(x)
print(y)

