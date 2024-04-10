from typing import List
import pandas as pd
import sys
sys.path.append('../extraction')
from extraction import *


def cleanLineDupilcates(data: List):
    df = pd.DataFrame(data)
    cleanDf = df.drop_duplicates()
    return cleanDf.to_dict(orient="records")

def cleanColumnDupilcates(data: List):
    df = pd.DataFrame(data)
    cleanDf = df.transpose().drop_duplicates().transpose()
    return cleanDf.to_dict(orient="records")

data = cleanColumnDupilcates(extractFromCSV("../../dataset/students.csv"))
print(pd.DataFrame(data))