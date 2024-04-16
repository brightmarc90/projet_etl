import pandas as pd
import json
import requests
import xml.etree.ElementTree as ET
import sqlite3
import os
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


# Fonction pour extraire les données de la base de données SQLite
def extractFromSQL(db, tb, url):

    # Chemin absolu du répertoire actuel
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Chemin absolu du fichier user.sql dans le répertoire actuel
    file_path = os.path.join(current_dir, url)

    try:
        # Supprimer la base de données si elle existe déjà
        conn = sqlite3.connect(f"{db}.db")
        c = conn.cursor()
        c.execute(f"DROP DATABASE IF EXISTS {db}")
    except sqlite3.Error as e:
        print(f"Erreur lors de la suppression de la base de données : {e}")

    try:
        # Connexion à la base de données SQLite
        conn = sqlite3.connect(f"{db}.db")
        c = conn.cursor()

        # Supprimer la table si elle existe déjà
        c.execute(f"DROP TABLE IF EXISTS {tb}")

        # Exécution du script SQL pour créer la table ou les tables
        with open(file_path, 'r') as script_file:
            sql_script = script_file.read()
            c.executescript(sql_script)

        # Lecture des données dans un DataFrame
        select_query = f'SELECT * FROM {tb}'
        df = pd.read_sql_query(select_query, conn)

        # Affichage des premières lignes du DataFrame
        print(df)
    except sqlite3.Error as e:
        print(f"Erreur lors de l'extraction des données : {e}")
    finally:
        # Fermeture de la connexion
        try:
            conn.close()
        except NameError:
            pass


# Appel de la fonction pour extraire les données de la base de données SQLite
extractFromSQL('personnage', 'users', '../data/sql/user.sql')

