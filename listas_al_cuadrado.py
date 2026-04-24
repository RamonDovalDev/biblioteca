# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def alcuadrado(lista):
    return [x**2 for x in lista]

print(alcuadrado([1, 2, 3, 4, 5]))
print (alcuadrado([1.5, 2.5, 3.5, 4.5, 5.5]))