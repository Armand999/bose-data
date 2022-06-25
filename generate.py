import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import pyplot
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram
from matplotlib.collections import LineCollection
#%matplotlib inline

import matplotlib.image as mpimg
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.decomposition import PCA
import random

##from json import dumpsdumps

import os
from datetime import datetime
from statistics import mean
from collections import Counter
from scipy import stats
from json import dumps


df = pd.read_csv("achat_enceinte.csv")
df.drop(columns=["Unnamed: 0", "Unnamed: 0.1"], inplace=True)

df = df.rename(columns={"COST":"COUT_TOTAL", "RESPONSABLE_ACHAT":"RESPONSABLE_ACHATS"})
 # Conversion de la puissance en int
df["PUISSANCE_WATT"] = df["PUISSANCE_WATT"].apply(lambda x: int(x.split(" ")[0]))
# Conversion des dates en format Datetime

df["DATE"] = df["DATE"].apply(lambda x: datetime.strptime(x,'%Y-%m-%d') if type(x) != float else x)
# Ajout de la colonne ANNEE

df["ANNEE"] =  df["DATE"].apply(lambda x: x.year if type(x) != float else x)
# Calcul du prix global d'achat par produit : VOLUME * PRIX_ACHAT


# Calcul du prix unitaire


df["PRIX_ACHAT"] = df["COUT_TOTAL"]/df["VOLUME"]
df["FOURNISSEUR"] = df["FOURNISSEUR"].apply(lambda x: x.split(" ")[-1])
df["FOURNISSEUR"] = df["FOURNISSEUR"].apply(lambda x: int(x))
# Arrondissement des prix d'achat

df["PRIX_ACHAT"] = round(df["PRIX_ACHAT"], 2)
df["PRIX_ACHAT"]
df["COULEUR"] = df["COULEUR"].apply(lambda x: x.replace("orrose", "or rose"))
df = pd.get_dummies(df, columns=['COULEUR'])
df["PAYS"] = df["PAYS"].apply(lambda x: x.title())
df["PAYS"] = df["PAYS"].apply(lambda x: x.replace("Alemagne", "Allemagne"))
df["PAYS"] = df["PAYS"].apply(lambda x: x.replace("Philippine", "Philippines"))
df["PAYS"] = df["PAYS"].apply(lambda x: x.replace("Philippiness", "Philippines"))
df["PAYS"] = df["PAYS"].apply(lambda x: x.replace("Soudan#", "Soudan"))

df = pd.get_dummies(df, columns=['PAYS'])
df["BLUETOOTH"] = df["BLUETOOTH"].apply(lambda x: x.title())
df["BLUETOOTH"] = df["BLUETOOTH"].apply(lambda x: 1 if x == "Vrai" else 0)
df["WATERPROOF"] = df["WATERPROOF"].apply(lambda x: 1 if x == True else 0)

 
df["RESPONSABLE_ACHATS"] = df["RESPONSABLE_ACHATS"].apply(lambda x: x.title())
df['RESPONSABLE_ACHATS'] = df['RESPONSABLE_ACHATS'].apply(lambda x : x.replace('Magnolia Biné', 'Magnolia Binet'))
df['RESPONSABLE_ACHATS'] = df['RESPONSABLE_ACHATS'].apply(lambda x : x.replace('Laure Pomerlo', 'Laure Pomerleau'))
df = pd.get_dummies(df, columns=['RESPONSABLE_ACHATS'])

df["MANAGER"] = df["MANAGER"].apply(lambda x: x.title())
df = pd.get_dummies(df, columns=['MANAGER'])
df.head()

df = df.drop(columns=["COUT_TOTAL", "DATE", "ANNEE", "LONGUEUR (inch)", "FOURNISSEUR"])
X = df.drop(columns=["PRIX_ACHAT"])
y = df["PRIX_ACHAT"]

X.to_csv("input.data.csv", index = False)

y.to_csv("ouput.data.csv", index = False)


