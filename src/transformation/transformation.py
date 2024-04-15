from typing import List
import pandas as pd
import sys
sys.path.append('../extraction')
from extraction import extractFromCSV
from updaters.updaters import *
from filters.filters import * 
from cleaners.cleaners import *   


data = cleanColumnDupilcates(extractFromCSV("../../dataset/students.csv"))
print(data)
"""#result1 = addColumn(data, ["Min", "Max", "Moyenne"])
#result2 = fillColumnByOps(result1, "Min", "min", ["Français", "Histoire"])
result2 = inferColumnType(data, ['Date de naissance'], "date")
result2 = cleanDateOutliers(result2)
result2 = inferColumnType(result2, ['Mathématiques', 'Français', 'Histoire'], "num")
result2 = correctNumOutliers(result2, ['Mathématiques', 'Français', 'Histoire'], "med")
result2 = normaliseCateg(result2, "Sexe", [("Homme", "H"), ("Femme", "F")])
print(pd.DataFrame(result2)) """
"""
faire 4 fonctions demain
    - inférence de type avec au moins 2 cas (str, date) => done
    - finaliser la fonction cleanDateOutliers => done
    - fonction de correction de valeurs numériques aberrantes (avec liste de colonnes en param) => done
    - fonction de normalisation de données ex: Homme Femme en H F
"""