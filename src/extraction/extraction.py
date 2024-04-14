import pandas as pd
import json
import requests
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
        while df.columns.size == 1:
            df = pd.json_normalize(df[df.columns[0]].iloc[0])
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

"""
fonction de transformation d'un noeud xml en dictionnaire
parms: 
    - child: le nœud à parcourir
returns:
    - un dictionnaire
"""    
def elementToDict(child):
    elmtDict = {}
    childList = []
    for elmt in child:
        if len(elmt) > 0:
            childList.append(elementToDict(elmt))
            elmtDict[elmt.tag] = childList
        else:
            elmtDict[elmt.tag] = elmt.text
    return elmtDict

"""
fonction d'extraction des données d'un xml
params:
    - filePath: chenmin vers le fichier
returns: 
    - une liste de dictionnaires
"""
def extractFromXML(filePath):
    try:
        tree = ET.parse(filePath)
        root = tree.getroot()
        data = []
        for child in root:
            data.append(elementToDict(child))
        df = pd.DataFrame(data)
        for column in df.columns:
            if(should_flatten(df[column].iloc[0])):
                df = flatten_column(df, column)
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None
    
def extractFromAPI(url):
    try:
        response = requests.get(url)
        # si réponse valide (200)
        if response.status_code == 200:
            # Retourne les données au format JSON
            data = response.json()
            df = pd.json_normalize(data) # traitement des données imbriquées
            while df.columns.size == 1:
                df = pd.json_normalize(df[df.columns[0]].iloc[0])
            for column in df.columns:
                if(should_flatten(df[column].iloc[0])):
                    df = flatten_column(df, column)
            return df.to_dict(orient='records')
        else:
            print(f"Erreur lors de la requête : {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur : {e}")
        return None
#test
#donnees = extractFromJson("../../dataset/test.json")
#donnees = extractFromAPI("http://localhost:3000/api/testimonials")
#print(pd.DataFrame(donnees))




