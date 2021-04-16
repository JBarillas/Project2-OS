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


    # Validar que la multiplicacion de matrices sea valida MatrixA * MatrixB, el numero de columnas de la matrix A debe ser igual al numero de filas de la matrix B
    if (len(dfMatrixA.columns) != len(dfMatrixB)):
        # Multiplicacion invalida
        print("Matrices no multiplicables")
        quit()

    # Hacer el pool de tareas (dividir y conquintar)
    #  Matrix A to a list of list
    list_rows_A = dfMatrixA.values.tolist()

    # Convert the rows of the Matrix B to a list of list
    df_transpose = dfMatrixB.T
    list_columns_B = df_transpose.values.tolist()

    startTime = time.time()

    with ThreadPoolExecutor(max_workers=nthreads) as executor:
        # executor.map(mulsum, list_rows_A, list_columns_B, len(dfMatrixB.columns))
        # Start the load operations and mark each future with its URL
        futures = []
        superList = []
        finalList = []
        position = 0
        for a in list_rows_A:
            futures.append(executor.submit(mulsum, a, list_columns_B, len(dfMatrixB.columns), position))  
            position += 1
        for future in concurrent.futures.as_completed(futures):
            superList.append(future.result())
        sorted_by_pos = sorted(superList, key=lambda tup: tup[0])
        for r in range(len(sorted_by_pos)):
            finalList.append(sorted_by_pos[r][1])
        finalDf = pd.DataFrame(finalList)
        # print(finalDf.head())
        finalDf.to_csv("{}".format(matrixC),index=False, header=False)
        endTime = time.time()
        print("\nElapsed time = {} seconds.".format(str(endTime - startTime)))
