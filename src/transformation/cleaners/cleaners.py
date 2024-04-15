import pandas as pd
import sys
sys.path.append('../../helpers')
from helpers.helpers import findDateOutliers

#cleanLineDupilcates
def cleanLineDupilcates(df: pd.DataFrame):
    cleanDf = df.drop_duplicates()
    return cleanDf

#cleanColumnDupilcates
def cleanColumnDupilcates(df: pd.DataFrame):
    cleanDf = df.transpose().drop_duplicates().transpose()
    return cleanDf

#cleanDateOutliers
def cleanDateOutliers(df: pd.DataFrame): 
    outliers = df.select_dtypes(include=['datetime64']).apply(findDateOutliers)
    return df[~(outliers.any(axis=1))]

def cleanData(df, script):
    functionName = globals().get(script)
    return functionName(df)
