import pandas as pd
import math
# pour les numériques
def isNumeric(valeur):
    try:
        float(valeur)
        return True
    except ValueError:
        return False

def eq(df, columns, constValue, result):
    r = result
    for elmt in columns:
        r = r & (df[elmt] == constValue)
    return df[r]

def neq(df, columns, constValue, result):
    r = result
    for elmt in columns:
        r = r & (df[elmt] != constValue)
    return df[r]

def gt(df, columns, constValue, result):
    r = result
    for elmt in columns:
        r = r & (df[elmt] > constValue)
    return df[r]

def gte(df, columns, constValue, result):
    r = result
    for elmt in columns:
        r = r & (df[elmt] >= constValue)
    return df[r]

def lt(df, columns, constValue, result):
    r = result
    for elmt in columns:
        r = r & (df[elmt] < constValue)
    return df[r]

def lte(df, columns, constValue, result):
    r = result
    for elmt in columns:
        r = r & (df[elmt] <= constValue)
    return df[r]

def nbCompare_case(df, columns, constValue, sign, result):
    switcher = {
        "eq": eq,
        "neq": neq,
        "gt": gt,
        "gte": gte,
        "lt": lt,
        "lte": lte
    }
    # récup de la fonction via le switcher
    func = switcher.get(sign, lambda: "Cas invalide")
    # Exécution de la fion
    return func(df, columns, constValue, result)

def minOfColumns(df, targetCol, columns):
    df[targetCol] = df[columns].apply(min, axis=1)
    return df

def maxOfColumns(df, targetCol, columns):
    df[targetCol] = df[columns].apply(max, axis=1)
    return df

def avgOfColumns(df, targetCol, columns):
    df[targetCol] = df[columns].mean(axis=1)
    return df

def columnOps_case(df, targetCol, opType, columns):
    switcher = {
        "min": minOfColumns,
        "max": maxOfColumns,
        "avg": avgOfColumns,
    }
    # récup de la fonction via le switcher
    func = switcher.get(opType, lambda: "Cas invalide")
    # Exécution de la fion
    return func(df, targetCol, columns)

def inferDateType(df, columns):
    for column in columns:
        df[column]= pd.to_datetime(df[column], errors='coerce')
    return df

def inferNumericType(df, columns):
    for column in columns:
        df[column]= pd.to_numeric(df[column], errors='coerce')
    return df

def inferStrType(df, columns):
    for column in columns:
        df[column]= df[column].astype(str)
    return df

def inferTypes_case(df, columns, destType):
    switcher = {
        "date": inferDateType,
        "str": inferStrType,
        "num": inferNumericType,
    }
    # récup de la fonction via le switcher
    func = switcher.get(destType, lambda: "Cas invalide")
    # Exécution de la fion
    return func(df, columns)

# Fonction pour détecter les valeurs aberrantes dans les colonnes numériques
def findNumOutliers(column, min, max):
    outliers = (column < min) | (column > max) | math.isnan(column)
    return outliers

# Fonction pour détecter les dates aberrantes
def findDateOutliers(column):
    #dates = pd.to_datetime(column, errors='coerce')
    return column.isna()

def useAvg(df, columns):
    for column in columns:
        outliers = df[column].apply(findNumOutliers, args=(0, 20))
        df.loc[outliers, column] = round(df[column].mean(), 2)
    return df

def useMedian(df, columns):
    for column in columns:
        outliers = df[column].apply(findNumOutliers, args=(0, 20))
        df.loc[outliers, column] = df[column].median()
    return df

def numOutliers_case(df, columns, method):
    switcher = {
        "avg": useAvg,
        "med": useMedian,
    }
    # récup de la fonction via le switcher
    func = switcher.get(method, lambda: "Cas invalide")
    # Exécution de la fion
    return func(df, columns)