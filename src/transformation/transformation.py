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