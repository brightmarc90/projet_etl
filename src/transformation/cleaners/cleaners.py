import pandas as pd
import sys
sys.path.append('../../helpers')
from helpers import findDateOutliers

def cleanLineDupilcates(df: pd.DataFrame):
    cleanDf = df.drop_duplicates()
    return cleanDf

def cleanColumnDupilcates(df: pd.DataFrame):
    cleanDf = df.transpose().drop_duplicates().transpose()
    return cleanDf

def cleanDateOutliers(df: pd.DataFrame): 
    outliers = df.select_dtypes(include=['datetime64']).apply(findDateOutliers)
    return df[~(outliers.any(axis=1))]