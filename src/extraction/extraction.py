import pandas as pd
import json
import xml.etree.ElementTree as ET
"""
fonction de test si un colonne doit être aplati
params:
    - field_value: valeur de la colonne à tester
return:
    - un booleen
"""
def should_flatten(field_value):
    return isinstance(field_value, (list, dict))

"""
fonction qui aplatit récursivement les données d'une colonne
params:
    - df: un dataframe
    - column_name: le nom de la colonne concernée
return: 
    - un dataframe avec les donnée
"""
def flatten_column(df, column_name):
    flattened_df = pd.json_normalize(df[column_name])
    # Renommer les colonnes aplaties pour éviter les conflits de noms
    flattened_df.columns = [f"{column_name}.{sub_column}" for sub_column in flattened_df.columns]
    for column in flattened_df.columns:
        if(should_flatten(flattened_df[column].iloc[0])):
            flattened_df = flatten_column(flattened_df, column)
    # Ajouter les colonnes aplaties au DataFrame d'origine
    return pd.concat([df, flattened_df], axis=1).drop(columns=[column_name])

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
        for column in df.columns:
            if(should_flatten(df[column].iloc[0])):
                df = flatten_column(df, column)
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

def extractFromXML(filePath):
    try:
        tree = ET.parse(filePath)
        root = tree.getroot()
        data = []
        for child in root:
            data.append({elmt.tag: elmt.text for elmt in child})
        df = pd.DataFrame(data)
        
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None
#test
donnees = extractFromCSV("../../dataset/school.csv")
print(pd.DataFrame(donnees))