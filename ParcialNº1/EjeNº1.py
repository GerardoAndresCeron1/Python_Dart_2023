"""
Obtener la determinante de una matriz de 3 x 3 con sus elementos aleatorios (5
al 10, enteros positivos). Se pueden utilizar librerías para resolver el algoritmo.
"""
import random
def matriz_random():
    matriz_1 = []
    for _ in range(3):
        fila = []
        for _ in range(3):
            fila.append(random.randint(5, 10))
        matriz_1.append(fila)
    return matriz_1

def cal_determinante(matriz_1):
    a = matriz_1[0][0]
    b = matriz_1[0][1]
    c = matriz_1[0][2]
    d = matriz_1[1][0]
    e = matriz_1[1][1]
    f = matriz_1[1][2]
    g = matriz_1[2][0]
    h = matriz_1[2][1]
    i = matriz_1[2][2]

    determinate = (a * e * i) + (b * f * g) + (c * d * h) - (c * e * g) - (b * d * i) - (a * f * h)
    return determinate

# Generar una matriz
matriz = matriz_random()

# imprimir la matriz
print("matriz 1:")
for fila in matriz:
    print(fila)

# Calculamos el determinante
determinante = cal_determinante(matriz)
print("El determinante es:", determinante)

