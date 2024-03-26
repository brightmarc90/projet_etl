import pandas as pd
import json

"""
fonction d'extraction de données d'un fichier json
params:
    - filePath: chemin vers le ficher
return:
    - une liste de dictionnaire
"""
def read_json(filePath):
    try:
        with open(filePath, 'r') as json_file:
            data = json.load(json_file)
        df = pd.json_normalize(data) # traitement des données imbriquées
        return df.to_dict(orient='records')
    except Exception as e:
        print("Erreur lors de la lecture du fichier")
        return None
    
#test
donnee = read_json("../../dataset/school.json")
print(pd.DataFrame(donnee))