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
def equalsTo(data: List, column, constValue):
    df = pd.DataFrame(data)
    result = df[column].isin(constValue)
    return dfToDict(df[result])

# valable pour les string et number
def notEqualsTo(data: List, column, constValue):
    df = pd.DataFrame(data)
    result = df[column].isin(constValue)
    return dfToDict(df[~result])

def strStartWith(data: List, column, constValue):
    df = pd.DataFrame(data)
    result = df[column].str.startswith(tuple(constValue))
    return dfToDict(df[result])

def strEndWith(data: List, column, constValue):
    df = pd.DataFrame(data)
    result = df[column].str.endswith(tuple(constValue))
    return dfToDict(df[result])

def strContains(data: List, column, constValue):
    df = pd.DataFrame(data)
    result = df[column].str.contains('|'.join(constValue))
    return dfToDict(df[result])

data = cleanColumnDupilcates(extractFromCSV("../../dataset/students.csv"))
result = strContains(data, "Nom", ["Mar", "Du"])
print(pd.DataFrame(result))