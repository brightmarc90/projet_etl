import pandas as pd
import sys
from helpers.helpers import findDateOutliers

#cleanLineDupilcates
def cleanLineDupilcates(df: pd.DataFrame):
    """
    Fonction d'élimination des doublons de lignes

    Args:
        df (pd.DataFrame): le dataframe des données à nettoyer

    Returns:
        pd.DataFrame: un dataframe
    """    
    cleanDf = df.drop_duplicates()
    return cleanDf

#cleanColumnDupilcates
def cleanColumnDupilcates(df: pd.DataFrame):
    """
    Fonction d'élimination des doublons de colonnes

    Args:
        df (pd.DataFrame): le dataframe des données à nettoyer

    Returns:
        pd.DataFrame: un dataframe
    """    
    cleanDf = df.transpose().drop_duplicates().transpose()
    return cleanDf

#cleanDateOutliers
def cleanDateOutliers(df: pd.DataFrame): 
    """
    Fonction qui élimine les lignes contenant des données aberrantes dans des colonnes de date

    Args:
        df (pd.DataFrame): le dataframe des données à nettoyer

    Returns:
        pd.DataFrame: un dataframe
    """    
    outliers = df.select_dtypes(include=['datetime64']).apply(findDateOutliers)
    return df[~(outliers.any(axis=1))]

def cleanData(df, script):
    """
    Fonction d'appel des fonction de nettoyage

    Args:
        df (pd.DataFrame): le dataframe des données à nettoyer
        script (string): le nom de la fonction à appeler

    Returns:
        pd.DataFrame: un dataframe
    """    
    functionName = globals().get(script)
    return functionName(df)
