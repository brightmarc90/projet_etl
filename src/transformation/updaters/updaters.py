import pandas as pd
from typing import List
import sys
from helpers.helpers import columnOps_case, inferTypes_case, numOutliers_case

def addColumn(df: pd.DataFrame, columns):
    """
    Fonction d'ajout de colonne à un dataframe

    Args:
        - df (pd.DataFrame): le dataframe à modifier
        - columns (List): liste des colonnes à ajouter

    Returns:
        pd.DataFrame: un dataframe
    """    
    if len(columns) > 0:
        for elmt in columns:
            df[elmt] = ""
    else:
        print("Votre liste de colonne à créer est vide")
    return df

def fillColumnByConst(df: pd.DataFrame, column, constValue):
    """
    Fonction d'affectation d'une constante à une colonne

    Args:
        - df (pd.DataFrame): le dataframe à modifier
        - column (string): le nom de colonne à remplir
        - constValue (any): valeur à mettre dans la colonne

    Returns:
        pd.DataFrame: un dataframe
    """    
    df[column] = constValue
    return df

def fillColumnByOps(df: pd.DataFrame, targetCol, opType, columns):
    """
    Fonction d'affectation de valeurs à une colonne sur la base d'opérations impliquant d'autres colonnes

    Args:
        - df (pd.DataFrame): le dataframe à modifier
        - targetCol (string): la colonne à remplir
        - opType (string): le type d'opération permettant de remplir la colonne (min, max, avg)
        - columns (List): liste des noms des colonnes intervenant dans l'opération

    Returns:
        pd.DataFrame: un dataframe
    """    
    return columnOps_case(df, targetCol, opType, columns)

def inferColumnType(df: pd.DataFrame, columns, destType): 
    """
    Fonction d'inférence de type

    Args:
        - df (pd.DataFrame): le dataframe à modifier
        - columns (List): liste des noms des colonnes à inférer
        - destType (string): le type à inférer à ces colonnes (str, date, num)

    Returns:
        pd.DataFrame: un dataframe
    """    
    return inferTypes_case(df, columns, destType)

def renameColumn(df: pd.DataFrame, changes: dict):
    """
    Fonction de renommage des entête de colonnes d'un dataframe

    Args:
        - df (pd.DataFrame): le dataframe à modifier
        - changes (dict): un dicitionnaire contenant les changements (ex: {"ColonneA": "ColonneB"}), ColonneA étant le nom d'origine de la - colonne et ColonneB le nouveau nom

    Returns:
        pd.DataFrame: un dataframe
    """    
    df = df.rename(columns=changes)
    return df

def correctNumOutliers(df: pd.DataFrame, columns, method): 
    """
    Fonction de correction des données numériques aberrantes par des méthodes bien précises

    Args:
        - df (pd.DataFrame): le dataframe à modifier
        - columns (List): Liste des noms des noms de colonnes à corriger
        - method (string): la méthode de correction des valeurs de ces colonnes (remplacer par la médiane (med) ou la moyenne (avg) par exemple)

    Returns:
        pd.DataFrame: un dataframe
    """    
    return numOutliers_case(df, columns, method)

def normaliseCateg(df: pd.DataFrame, column, changes: dict):
    """
    Fonction de normalisation de données catégorielles

    Args:
        - df (pd.DataFrame): le dataframe à modifier
        - column (string): le nom de la colonne à modifier
        - changes (dict): uun dicitionnaire contenant les changements (ex: {"Homme": "H"}), Homme étant la valeur d'origine et H la nouvelle valeur

    Returns:
        pd.DataFrame: un dataframe
    """    
    df[column] = df[column].map(changes).fillna(df[column])
    return df