import random

def sol_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        columna = []
        for j in range(columnas):
            elementos = random.randint(0, 5)
            columna.append(elementos)
        matriz.append(columna)
    return matriz

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

def m3_multi(resultado, m3):
    filas = len(m3)
    columnas = len(m3[0])
    resultado_final = []

    for i in range(columnas):
        columna = []
        for j in range(filas):
            elementos = resultado[i][j] * m3[i][j]
            columna.append(elementos)
        resultado_final.append(columna)
    return resultado_final

# Le pregunta al usuario el numero de filas y columnas que tendra cada matriz
filas = int(input("Ingrese los valores de la fila para la matriz: "))
columnas = int(input("Ingrese los valores de la columna para la matriz: "))
filas = int(input("Ingrese los valores de la fila para la matriz 3: "))
columnas = int(input("Ingrese los valores de la columna para la matriz 3: "))

# Crear ambas matrices
print("Creando matriz 1...")
m1 = sol_matriz(filas, columnas)
print("Creando matriz 2...")
m2 = sol_matriz(filas, columnas)
print("Creando matriz 3...")
m3 = sol_matriz(filas, columnas)

mat_sum = m1_suma(m1,m2)
print("La suma de las dos matrices es: ")
for filas in mat_sum:
    print(filas)

mat_multi = m3_multi(mat_sum, m3)
print("La multiplicación de las dos matrices es: ")
for filas in mat_multi:
    print(filas)