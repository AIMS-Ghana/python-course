__author__ = 'cap10'

def test_euler_11():
    assert False

import csv
import numpy as np

def euler_11():
    maxprod = 0
    with open("euler_11.csv",'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=" ")
        input = [row for row in reader]
        inputarray = np.array(input).astype(int)
        # loop rows
        # transpose, loop cols
        # loop corner indices, calculate diagonals
    return maxprod


print(euler_11())