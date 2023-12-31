import pymongo
import pandas as pd

# Connexion à MongoDB
client = pymongo.MongoClient("mongodb+srv://SDCr7AqKRHFk6YEh:XjBIRuxMb3nHurPD@cluster0.deqk5dg.mongodb.net/")
db = client["Spotify"]
collection = db["spotify"]

# Récupération des documents
documents = collection.find({}, {"audio_features", "audio_analysis"})

# Conversion des documents en une liste de dictionnaires
documents_list = list(documents)

# Utilisation de json_normalize pour transformer les clés en colonnes
# Cela suppose que 'audio_features' est un dictionnaire
df = pd.json_normalize(documents_list)

# Affichage des premières lignes du DataFrame
print(df.columns)
print(df.head())
