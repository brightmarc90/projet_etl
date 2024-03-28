import pandas as pd
import json

"""
fonction d'extraction de données d'un fichier json
params:
    - filePath: chemin vers le ficher
return:
    - une liste de dictionnaire
"""
def extractFromJson(filePath):
    try:
        with open(filePath, 'r') as json_file:
            data = json.load(json_file)
        df = pd.json_normalize(data) # traitement des données imbriquées
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None

"""
fonction d'extraction de données d'un fichier csv
params:
    - filePath: chemin vers le ficher
return:
    - une liste de dictionnaire
"""
def extractFromCSV(filePath):
    try:
        df = pd.read_csv(filePath)
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None
    
#test
donnees = extractFromJson("../../dataset/school.json")
print(pd.DataFrame(donnees))