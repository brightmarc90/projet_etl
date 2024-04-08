import yaml
import pandas as pd
from extraction.extraction import *

# Lecture du fichier YAML
with open("etl.yaml", "r") as file:
    data = yaml.safe_load(file)

results = []
# Parcourir les étapes et exécuter les fonctions
for step in data['steps']:
    print(f"===> Etape: {step['name']} <=== \n")
    for function in step['functions']:
        #
        functionName = globals().get(function['name'])
        if functionName:
            results = functionName(**function.get('params', {}))
            print(pd.DataFrame(results))
        else:
            print(f"Erreur: La fonction {function['name']} n'existe pas.")
