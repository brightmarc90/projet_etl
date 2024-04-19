import pandas as pd
import sys
from helpers.helpers import isNumeric, nbCompare_case

# Valable pour les strings
def equalsTo(df: pd.DataFrame, columns, constValues):
    """
    Fonction qui filtre un dataframe selon le critère d'égalité

    Args:
        - df (pd.DataFrame): le dataframe à filtrer
        - columns (List): liste des noms des colonnes dont les valeurs seront comparées
        - constValues (List): liste des valeurs de comparaison

    Returns:
        pd.DataFrame: un dataframe
    """    
    result = True
    for elmt in columns:
        result = result & df[elmt].isin(constValues)
    return df[result]

def notEqualsTo(df: pd.DataFrame, columns, constValues):
    """
    Fonction qui filtre un dataframe selon le critère d'inégalité

    Args:
        - df (pd.DataFrame): le dataframe à filtrer
        - columns (List): liste des noms des colonnes dont les valeurs seront comparées
        - constValues (List): liste des valeurs de comparaison

    Returns:
        pd.DataFrame: un dataframe
    """    
    result = True
    for elmt in columns:
        result = result & df[elmt].isin(constValues)
    return df[~result]

def strStartWith(df: pd.DataFrame, columns, constValues):
    """
    Fonction qui filtre un dataframe sur des chaines de caractères commençant par des valeurs précises

    Args:
        - df (pd.DataFrame): le dataframe à filtrer
        - columns (List): liste des noms des colonnes dont les valeurs seront comparées
        - constValues (List): liste des chaines qui doivent commencer les chaines à comparer

    Returns:
        pd.DataFrame: un dataframe
    """    
    result = True
    for elmt in columns:
        result = result & df[elmt].str.startswith(tuple(constValues))
    return df[result]

def strEndWith(df: pd.DataFrame, columns, constValues):
    """
    Fonction qui filtre un dataframe sur des chaines de caractères se terminant par des valeurs précises

    Args:
        - df (pd.DataFrame): le dataframe à filtrer
        - columns (List): liste des noms des colonnes dont les valeurs seront comparées
        - constValues (List): liste des chaines qui doivent terminer les chaines à comparer

    Returns:
        pd.DataFrame: un dataframe
    """    
    result = True

    for elmt in columns:
        result = result & df[elmt].str.endswith(tuple(constValues))
        
    return df[result]

def strContains(df: pd.DataFrame, columns, constValues):
    """
    Fonction qui filtre un dataframe sur des colonnes contenant des valeurs bien précises

    Args:
        - df (pd.DataFrame): le dataframe à filtrer
        - columns (List): liste des noms des colonnes dont les valeurs seront comparées
        - constValues (List): liste des chaines que doivent contenir les chaines à comparer

    Returns:
        pd.DataFrame: un dataframe
    """    
    result = True
    for elmt in columns:
        result = result & df[elmt].str.contains('|'.join(constValues))
    return df[result]

def nbCompare(df: pd.DataFrame, columns, constValue, sign):
    """
    Fonction qui filtre un dataframe sur des critère de comparaison de valeurs numériques

    Args:
        - df (pd.DataFrame): le dataframe à filtrer
        - columns (List): liste des noms des colonnes dont les valeurs seront comparées
        - constValue (numeric): la valeur à comparer aux valeurs des colonnes
        - sign (string): le sens de la comparaison (égalité (eq), supériorité (gt), ...)

    Returns:
        pd.DataFrame: un dataframe
    """    
    if isNumeric(constValue):
        result = True
        return nbCompare_case(df, columns, constValue, sign, result)
    else:
        print("Merci de préciser une valeur de comparaison numérique")
        return None