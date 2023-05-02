"""
Crear dos matrices solicitando los datos por consola (cantidad de filas y columnas), 
y los elementos de estas matrices deben ser aleatorios del 1 al 5, no se deben ingresar por consola. 
Luego se deben sumar en una función las matrices, y en otra función restarlas.
En este caso no se puede utilizar numpy, solo estructuras propias de Python
"""

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

# Funcion para restar una segunda matriz
def m1_resta(m1,m2):
    filas = len(m1)
    columnas = len(m1[0])
    resultado = []

    for i in range(columnas):
        columna = []
        for j in range(filas):
            elementos = m1[i][j] - m2[i][j]
            columna.append(elementos)
        resultado.append(columna)
    return resultado

# Le pregunta al usuario el numero de filas y columnas que tendra cada matriz
filas = int(input("Ingrese los valores de la fila para la matriz: "))
columnas = int(input("Ingrese los valores de la columna para la matriz: "))

# Crear ambas matrices
print("Creando matriz 1...")
m1 = sol_matriz(filas, columnas)
print("Creando matriz 2...")
m2 = sol_matriz(filas, columnas)

mat_sum = m1_suma(m1,m2)
print("La suma de las dos matrices es: ")
for filas in mat_sum:
    print(filas)

mat_rest = m1_resta(m1,m2)
print("La resta de las dos matrices es: ")
for filas in mat_rest:
    print(filas)