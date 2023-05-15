"""
numeros = input("Ingresa los números separados por comas: ")
lista_numeros = [int(numero) for numero in numeros.split(",")]
suma = sum(lista_numeros)
print("La suma de los elementos de la lista es:", suma)
"""
import numpy as np

matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
escalar = 2

resultado1 = np.matmul(matriz1, matriz2)

print("Matriz 1:\n", matriz1)
print("Matriz 2:\n", matriz2)
print("Resultado de la multiplicación de matrices:\n", resultado1)

resultado2 = np.multiply(matriz1, escalar)

print("Matriz original:\n", matriz1)
print("Escalar:\n", escalar)
print("Resultado:\n", resultado2)

print("Forma de la matriz:\n", np.shape(matriz1))