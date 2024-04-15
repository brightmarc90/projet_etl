from typing import List
import pandas as pd
import sys
sys.path.append('../extraction')
import os

def loadInJsonOrXML(data: List, destPath, fileName, fileType):
    df = pd.DataFrame(data)
    # Vérifier si le dossier de destination existe, sinon le créer
    if not os.path.exists(destPath):
        os.makedirs(destPath)
    if(fileType == "JSON"):
        pathToFile = os.path.join(destPath, fileName+".json")
        df.to_json(pathToFile, orient="records", indent=4)
    else:
        pathToFile = os.path.join(destPath, fileName+".xml")
        df.to_xml(pathToFile, root_name="data", row_name="element")
