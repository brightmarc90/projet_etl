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

# valable pour les string et number
def equalsTo(data: List, columns, constValues):
    df = pd.DataFrame(data)
    result = True
    for elmt in columns:
        result = result & df[elmt].isin(constValues)
    return dfToDict(df[result])

# valable pour les string et number
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

data = cleanColumnDupilcates(extractFromCSV("../../dataset/students.csv"))
result = strContains(data, ["Nom", "Prénom"], ["d", "a"])
print(pd.DataFrame(result))