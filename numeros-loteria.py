# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
awarded_numbers = []
for i in range(6):
    awarded_numbers.append(int(input("Introduce un número ganador: ")))
awarded_numbers.sort();

print (awarded_numbers)
