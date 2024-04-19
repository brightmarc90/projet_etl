from typing import List
import pandas as pd
import sys
sys.path.append('../extraction')
import os

def loadInJsonOrXML(df: pd.DataFrame, destPath, fileName, fileType):   
    """
    Fonction d'enregistrment des données transformées dans le format 

    Args:
        - df (pd.DataFrame): dataframe contenant les données transformées
        - destPath (string): chemin de destination du fichier
        - fileName (string): nom sous lequel sera enregistré le fichier
        - fileType (string): extension du fichier de destination
    """
    # Vérifier si le dossier de destination existe, sinon le créer
    if not os.path.exists(destPath):
        os.makedirs(destPath)
    if(fileType == "JSON"):
        pathToFile = os.path.join(destPath, fileName+".json")
        df.to_json(pathToFile, orient="records", indent=4)
    else:
        pathToFile = os.path.join(destPath, fileName+".xml")
        df.to_xml(pathToFile, root_name="data", row_name="element")
