import pandas as pd
from typing import List
import sys
sys.path.append('../helpers')
from helpers import columnOps_case, inferTypes_case, numOutliers_case

def addColumn(df: pd.DataFrame, columns):
    if len(columns) > 0:
        for elmt in columns:
            df[elmt] = ""
    else:
        print("Votre liste de colonne à créer est vide")
    return df

def fillColumnByConst(df: pd.DataFrame, column, constValue):
    df[column] = constValue
    return df

def fillColumnByOps(df: pd.DataFrame, targetCol, opType, columns):
    return columnOps_case(df, targetCol, opType, columns)

def inferColumnType(df: pd.DataFrame, columns, destType): 
    return inferTypes_case(df, columns, destType)

def renameColumn(df: pd.DataFrame, changes: dict):
    df = df.rename(columns=changes)
    return df

def correctNumOutliers(df: pd.DataFrame, columns, method): 
    return numOutliers_case(df, columns, method)

def normaliseCateg(df: pd.DataFrame, column, changes: List[tuple]):
    for change in changes:
        df.loc[df[column] == change[0], column] = change[1]
    return df