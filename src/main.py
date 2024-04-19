import yaml
import pandas as pd
from extraction.extraction import extractData
from transformation.cleaners.cleaners import *
from transformation.updaters.updaters import *
from loading.loading import *

# Lecture du fichier YAML
with open("etl.yaml", "r") as file:
    data = yaml.safe_load(file)

results = []
# Parcourir les étapes et exécuter les fonctions
for job in data['jobs']:
    print(f"===> {job['name']}: {job['description']} <=== \n")
    for step in job['steps']:
        print(f"\n ===> {step['name']} <=== \n")
        if(step['type'] == "Extraction"):
            if (step['source'] == 'API'):
                results = extractData(source=step['source'], url=step['url'])
            else:
                results = extractData(source=step['source'], filePath=step['filePath'])
            print(results)
        if(step['type'] == "Transformation"):
            for change in step['changes']:
                if(change['type'] == "clean"):
                    results = cleanData(results, change['script'])
                if(change['type'] == "update"):
                    functionName = globals().get(change['script'])
                    results = functionName(results, **change.get('params', {}))
                if(change['type'] == "filter"):
                    pass
            print(results)
        if(step['type'] == "Loading"):
            if(step['params']['fileType'] == "BD"):
                pass
            else:
                results = loadInJsonOrXML(results, **step.get('params', {}))