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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fileA", help='Name of the CSV file for Matrix A')
    parser.add_argument("fileB", help='Name of the CSV file for Matrix B')
    parser.add_argument("poolSize", type=int, help='Number of threads in the pool')
    parser.add_argument("fileC", help='Name of the CSV file for the resulting Matix')

    args = parser.parse_args()
    # Capturando los argumentos
    matrixA = str(args.fileA)
    matrixB = str(args.fileB)
    matrixC = str(args.fileC)
    nthreads = args.poolSize

    dfMatrixA = pd.read_csv(matrixA, header=None)
    dfMatrixB = pd.read_csv(matrixB,  header=None)

