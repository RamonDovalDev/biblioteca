# Crea una lista e inicalizala con 5 cadenas de caracteres leídas por teclado. 
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra 
# sus elementos  por la pantalla.

lista1 = []
lista2 = []
# Recorro la lista y leo cada elemento por teclado
for i in range(1, 6):
    lista1.append(input("Dame la cadena %d: " % i))

# Copiar lista obtenida en orden inverso
lista2 = lista1[::-1]

# Recorro lista2 para imprimirla en pantalla
for cadena in lista2:
    print(cadena)