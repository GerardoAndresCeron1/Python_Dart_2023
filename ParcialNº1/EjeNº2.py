"""
Crear dos matrices donde la cantidad de filas y columnas serán 3 x 3. Los
elementos de estas matrices deben ser generados de forma aleatoria (-5 a -10).
Luego se deben multiplicar ambas matrices e imprimir la matriz resultante.
Agregar una condición para que las dimensiones sean acordes para realizar la
multiplicación entre ambas matrices.
Esta matriz resultado se debe multiplicar por una matriz identidad, e imprimir la matriz final.
Se pueden utilizar librerías para resolver todo el ejercicio.
"""

import random
import numpy as np

def matriz_random1():
    matriz_1 = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(random.randrange(0,-10,-5))
        matriz_1.append(fila)
    return matriz_1

def matriz_random2():
    matriz_2 = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(random.randrange(0,-10,-5))
        matriz_2.append(fila)
    return matriz_2

# Generar una matriz
matriz = matriz_random1()

# imprimir la matriz
print("matriz 1:")
for fila in matriz:
    print(fila)

# Generar una matriz
matriz__2 = matriz_random2()

# imprimir la matriz
print("matriz 2:")
for fila in matriz__2:
    print(fila)


def matriz_multi(matriz, matriz__2):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []

    for i in range(columnas):
        columna = []
        for j in range(filas):
            elemento = matriz[i][j] * matriz__2[i][j]
            columna.append(elemento)
        resultado.append(columna)
    return resultado

mat_multi = matriz_multi(matriz, matriz__2)

# imprimir la matriz
print("La multiplicación entre las dos matrices")
for fila in mat_multi:
    print(fila)
