if _name_ == "_main_":
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