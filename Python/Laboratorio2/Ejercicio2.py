import random

# Le pregunta al usuario el numero de filas y columnas que tendra cada matriz
filas = int(input("Ingrese los valores de la fila para la matriz: "))
columnas = int(input("Ingrese los valores de la columna para la matriz: "))
escalar = int(input("Ingrese el valor del escalar: "))

def sol_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        columna = []
        for j in range(columnas):
            elementos = random.randint(0, 10)
            columna.append(elementos)
        matriz.append(columna)
    return matriz

def m1_multi(m1, escalar):
    filas = len(m1)
    columnas = len(m1[0])
    resultado = []

    for i in range(columnas):
        columna = []
        for j in range(filas):
            elementos = m1[i][j] * escalar
            columna.append(elementos)
        resultado.append(columna)
    return resultado

print("Creando matriz 1...")
m1 = sol_matriz(filas, columnas)

mat_multi = m1_multi(m1, escalar)
print("La multiplicación de las dos matrices es: ")
for filas in mat_multi:
    print(filas)