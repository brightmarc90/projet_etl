import pandas as pd
import sys
sys.path.append('../../helpers')
from helpers import isNumeric, nbCompare_case

# valable pour les string
def equalsTo(df: pd.DataFrame, columns, constValues):
    result = True
    for elmt in columns:
        result = result & df[elmt].isin(constValues)
    return df[result]

def notEqualsTo(df: pd.DataFrame, columns, constValues):
    result = True
    for elmt in columns:
        result = result & df[elmt].isin(constValues)
    return df[~result]

def strStartWith(df: pd.DataFrame, columns, constValues):
    result = True
    for elmt in columns:
        result = result & df[elmt].str.startswith(tuple(constValues))
    return df[result]

def strEndWith(df: pd.DataFrame, columns, constValues):
    result = True
    for elmt in columns:
        result = result & df[elmt].str.endswith(tuple(constValues))
    return df[result]

def strContains(df: pd.DataFrame, columns, constValues):
    result = True
    for elmt in columns:
        result = result & df[elmt].str.contains('|'.join(constValues))
    return df[result]

def nbCompare(df: pd.DataFrame, columns, constValue, sign):
    if isNumeric(constValue):
        result = True
        return nbCompare_case(df, columns, constValue, sign, result)
    else:
        print("Merci de préciser une valeur de comparaison numérique")
        return None