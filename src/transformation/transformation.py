""" from typing import List
import pandas as pd
import sys
from src.extraction.extraction import extractFromCSV
from src.transformation.updaters.updaters import *
from src.transformation.filters.filters import * 
from cleaners.cleaners import *   


data = cleanColumnDupilcates(extractFromCSV("../../dataset/students.csv"))
print(data) """