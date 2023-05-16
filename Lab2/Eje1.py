import random
# Creando la lista vacia para crear la matriz
def matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        columna = []
        for j in range(columnas):
            elementos = random.randint(1, 5)
            columna.append(elementos)
        matriz.append(columna)
    return matriz

def n_matriz(filas1, columnas1):
    matriz1 = []
    for i in range(filas1):
        columna = []
        for j in range(columnas1):
            elementos = int(input(f"Ingrese los valores para la matriz [{i}[{j}]] : "))
            columna.append(elementos)
        matriz1.append(columna)
    return matriz1

# Funcion para sumar una segunda matriz
def m1_suma(m1,m2):
    filas = len(m1)
    columnas = len(m1[0])
    resultado = []

    for i in range(columnas):
        columna = []
        for j in range(filas):
            elementos = m1[i][j] + m2[i][j]
            columna.append(elementos)
        resultado.append(columna)
    return resultado

def matriz_multi(mat_sum, escalar):
    matrix_multi = mat_sum * escalar
    print(matrix_multi)

def mat_multi(matrix_multi, m3):
    filas1 = len(m3)
    columnas1 = len(m3[0])
    result = []

    for i in range(columnas1):
        columna = []
        for j in range(filas1):
            elementos = matrix_multi * m3[i][j]
            columna.append(elementos)
        result.append(columna)
    return result

# Le pregunta al usuario el numero de filas y columnas que tendra cada matriz
filas = int(input("Ingrese los valores de la fila para la matriz: "))
columnas = int(input("Ingrese los valores de la columna para la matriz: "))
escalar = int(input("Ingrese el valor para el escalar: "))

# Le pregunta al usuario el numero de filas y columnas que tendra la nueva matriz
filas = int(input("Ingrese los valores de la fila para la nueva matriz: "))
columnas = int(input("Ingrese los valores de la columna para la nueva matriz: "))

# Crear ambas matrices
print("Creando matriz 1...")
m1 = matriz(filas, columnas)
print("Creando matriz 2...")
m2 = matriz(filas, columnas)
print("Creando matriz 3...")
m3 = matriz(filas, columnas)

# imprime la suma de las 2 primeras matrices
mat_sum = m1_suma(m1, m2)
print("La suma de las dos matrices es: ")
for filas in mat_sum:
    print(filas)
