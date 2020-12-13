import os
import numpy as np

def preprocess_data():
    data = np.empty((39,1))
    with open('kddcup.data_10_percent_corrected', 'r') as file:
        lines = file.readlines()
        x = 0
        count = np.zeros((42), dtype=float)
        for line in lines:
            items = line.split(",")
            if x == 0:
                first = items
            for i in range(42):
                if first[i] == items[i]:
                    count[i] = count[i] + 1
            x = x + 1
    count = count / x
    for i in range(42):
        if float(count[i]) <= 0.80:
            print(i)
    print(count)

preprocess_data()
