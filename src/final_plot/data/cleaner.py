import pandas as pd
import csv
import numpy as np


file = open('feeds.csv', 'rb')
data = pd.load_csv(file)
file.close()

#for cleaning NaN valuues/ 0 values
university_towns = []
with open('Datasets/university_towns.txt') as file:
    for line in file:
        if 'NaN' in line:
            # Remember this `state` until the next is found
            state = line
        else:
            # Otherwise, we have a city; keep `state` as last-seen
            university_towns.append((state, line))

#replcing Nan
from numpy import NaN
frame.replace({NaN:0.00})
