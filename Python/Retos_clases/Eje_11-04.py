"""
Escribir un programa que pida al usuario una palabra
y que muestre por consola el número de veces que 
contiene cada vocal
"""

palabra = input("ingrese una palabra: ")

a = 0
e = 0
i = 0
o = 0
u = 0
for letra in palabra:
    if letra.lower() == "a":
        a += 1
    elif letra.lower() == "e":
        e += 1
    elif letra.lower() == "i":
        i += 1
    elif letra.lower() == "o":
        o += 1
    elif letra.lower() == "u":
        u += 1
    
print("La palabra contiene '{}':".format(palabra))
print("- {} 'a' vocales".format(a))
print("- {} 'e' vocales".format(e))
print("- {} 'i' vocales".format(i))
print("- {} 'o' vocales".format(o))
print("- {} 'u' vocales".format(u))