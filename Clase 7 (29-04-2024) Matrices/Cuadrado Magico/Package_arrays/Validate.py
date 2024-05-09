def validar_cuadrado_magico (M: int, N: int) -> int:
    M = int(M)
    N = int(N)
    while M != N:
        M = int(input("Error.Reingrese cantidad de filas: "))
        N = int(input("Error.Reingrese cantidad de columnas: "))
    return M, N