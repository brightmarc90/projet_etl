import pandas as pd
import json
import requests
import xml.etree.ElementTree as ET

def should_flatten(field_value):        
    """
    Fonction de test si un colonne doit être aplati

    Args:
        field_value: valeur de la colonne à tester

    Returns:
        booléen
    """
    return isinstance(field_value, (list, dict))

def flatten_column(df, column_name):
    """
    Fonction qui aplatit récursivement les données d'une colonne

    Args:
        - df (dataframe): un dataframe
        - column_name (string): le nom de la colonne concernée

    Returns: 
        pd.DataFrame: un dataframe
    """
    flattened_df = pd.json_normalize(df[column_name])
    # Renommer les colonnes aplaties pour éviter les conflits de noms
    flattened_df.columns = [f"{column_name}.{sub_column}" for sub_column in flattened_df.columns]
    for column in flattened_df.columns:
        if(should_flatten(flattened_df[column].iloc[0])):
            flattened_df = flatten_column(flattened_df, column)
    # Ajouter les colonnes aplaties au DataFrame d'origine
    return pd.concat([df, flattened_df], axis=1).drop(columns=[column_name])


def extractFromJson(filePath):
    """
    Fonction d'extraction de données d'un fichier json

    Args:
        filePath (string): chemin vers le ficher

    return:
        pd.DataFrame: un dataframe
    """
    try:
        with open(filePath, 'r') as json_file:
            data = json.load(json_file)
        df = pd.json_normalize(data) # traitement des données imbriquées
        while df.columns.size == 1:
            df = pd.json_normalize(df[df.columns[0]].iloc[0])
        for column in df.columns:
            if(should_flatten(df[column].iloc[0])):
                df = flatten_column(df, column)
        return df
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None

def extractFromCSV(filePath):
    """
    Fonction d'extraction de données d'un fichier csv

    Args:
        filePath (string): chemin vers le ficher

    return:
        pd.DataFrame: un dataframe
    """
    try:
        df = pd.read_csv(filePath)
        return df
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None
  
def elementToDict(child):
    """
    Fonction de transformation d'un noeud xml en dictionnaire

    Args: 
        child: le nœud à parcourir

    returns:
        Un dictionnaire
    """  
    elmtDict = {}
    childList = []
    for elmt in child:
        if len(elmt) > 0:
            childList.append(elementToDict(elmt))
            elmtDict[elmt.tag] = childList
        else:
            elmtDict[elmt.tag] = elmt.text
    return elmtDict

def extractFromXML(filePath):
    """
    Fonction d'extraction des données d'un fichier xml

    Args:
        filePath (string): chemin vers le fichier

    returns: 
        pd.DataFrame: un dataframe
    """
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
        return df
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None
    
def extractFromAPI(url):
    """
    Fonction d'extraction des données d'une API

    Args:
        url (string): lien vers l'API

    returns: 
        pd.DataFrame: un dataframe
    """
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
            return df
        else:
            print(f"Erreur lors de la requête : {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur : {e}")
        return None
    
def extractData(source, filePath=None, url=None):
    """
    Fonction permettant d'exécuter une fonction d'extraction de données selon une source bien définie

    Args:
        source (string): le type de la source de données, plusieurs types sont disponibles: CSV, XML, JSON, API

    returns: 
        pd.DataFrame: un dataframe
    """
    if (source == "CSV"):
        return extractFromCSV(filePath)
    if (source == "XML"):
        return extractFromXML(filePath)
    if (source == "JSON"):
        return extractFromJson(filePath)
    if (source == "API"):
        return extractFromAPI(url)

#test
#donnees = extractFromJson("../../dataset/test.json")
#donnees = extractFromAPI("http://localhost:3000/api/testimonials")
#print(pd.DataFrame(donnees))