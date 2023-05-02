"""
Crear dos matrices solicitando los datos por consola (cantidad de filas y columnas),y se debe añadir uno por uno los elementos de ambas matrices. 
Luego se deben sumar estas matrices en una función, y en otra función restarlas. Solo utilizando las funciones de la biblioteca numpy.
"""
# crear una funcion para crear una matriz
def sol_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        columna = []
        for j in range(columnas):
            elementos = int(input(f"ingrese los elementos de la matriz [{i}[{j}]] : "))
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
            elemento = m1[i][j] + m2[i][j]
            columna.append(elemento)
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
            elemento = m1[i][j] - m2[i][j]
            columna.append(elemento)
        resultado.append(columna)
    return resultado

# Le pregunta al usuario el numero de filas y columnas que tendra cada matriz
filas = int(input("Ingrese los valores de la fila para la matriz: "))
columnas = int(input("Ingrese los valores de la columna para la matriz: "))

# Crear ambas matrices
print("ingrese elementos para la primera matriz: ")
m1 = sol_matriz(filas, columnas)
print("ingrese elementos para la primera matriz: ")
m2 = sol_matriz(filas, columnas)

mat_sum = m1_suma(m1,m2)
print("La suma de las dos matrices is: ")
for filas in mat_sum:
    print(filas)

mat_rest = m1_resta(m1,m2)
print("La resta de las dos matrices is: ")
for filas in mat_rest:
    print(filas)