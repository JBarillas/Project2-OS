import argparse
import pandas as pd
import numpy as np 
from concurrent.futures import ThreadPoolExecutor
import sys
import time
import concurrent.futures

def mulsum(array1, array2, ncolumnsB, pos):
    finalMatrix = []
    row = np.array(array1)
    for i in range(ncolumnsB):
        colum = np.array(array2[i])
        finalMatrix.append(np.dot(row,colum))
    return (pos, finalMatrix)

