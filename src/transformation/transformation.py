from typing import List
import pandas as pd
import sys
sys.path.append('../extraction')
from extraction import extractFromCSV

def dfToDict(data: pd.DataFrame):
    return data.to_dict(orient="records")

def cleanLineDupilcates(data: List):
    df = pd.DataFrame(data)
    cleanDf = df.drop_duplicates()
    return dfToDict(cleanDf)

def cleanColumnDupilcates(data: List):
    df = pd.DataFrame(data)
    cleanDf = df.transpose().drop_duplicates().transpose()
    return dfToDict(cleanDf)

# valable pour les string
def equalsTo(data: List, columns, constValues):
    df = pd.DataFrame(data)
    result = True
    for elmt in columns:
        result = result & df[elmt].isin(constValues)
    return dfToDict(df[result])

def notEqualsTo(data: List, columns, constValues):
    df = pd.DataFrame(data)
    result = True
    for elmt in columns:
        result = result & df[elmt].isin(constValues)
    return dfToDict(df[~result])

def strStartWith(data: List, columns, constValues):
    df = pd.DataFrame(data)
    result = True
    for elmt in columns:
        result = result & df[elmt].str.startswith(tuple(constValues))
    return dfToDict(df[result])

def strEndWith(data: List, columns, constValues):
    df = pd.DataFrame(data)
    result = True
    for elmt in columns:
        result = result & df[elmt].str.endswith(tuple(constValues))
    return dfToDict(df[result])

def strContains(data: List, columns, constValues):
    df = pd.DataFrame(data)
    result = True
    for elmt in columns:
        result = result & df[elmt].str.contains('|'.join(constValues))
    return dfToDict(df[result])

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
    return dfToDict(df[r])

def neq(df, columns, constValue, result):
    r = result
    for elmt in columns:
        r = r & (df[elmt] != constValue)
    return dfToDict(df[r])

def gt(df, columns, constValue, result):
    r = result
    for elmt in columns:
        r = r & (df[elmt] > constValue)
    return dfToDict(df[r])

def gte(df, columns, constValue, result):
    r = result
    for elmt in columns:
        r = r & (df[elmt] >= constValue)
    return dfToDict(df[r])

def lt(df, columns, constValue, result):
    r = result
    for elmt in columns:
        r = r & (df[elmt] < constValue)
    return dfToDict(df[r])

def lte(df, columns, constValue, result):
    r = result
    for elmt in columns:
        r = r & (df[elmt] <= constValue)
    return dfToDict(df[r])

def switch_case(df, columns, constValue, sign, result):
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

def nbCompare(data: List, columns, constValue, sign):
    if isNumeric(constValue):
        df = pd.DataFrame(data)
        result = True
        return switch_case(df, columns, constValue, sign, result)
    else:
        print("Merci de préciser une valeur de comparaison numérique")
        return None
    
data = cleanColumnDupilcates(extractFromCSV("../../dataset/students.csv"))
result = nbCompare(data, ["Physique", "Français"], 13, "neq")
print(pd.DataFrame(result))