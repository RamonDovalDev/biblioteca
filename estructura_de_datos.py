"""
* EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""
# Listas
lista = ["Leviathan", "Xasthur", "Shining", "Lifelover"]
print(lista)
lista.append("Type O Negative") # Inserción
print(lista)
lista.remove("Xasthur")
print(lista)
print(lista[0]) # Acceso
lista[1] = "Gaerea"
print(lista)
lista.sort() # Ordenación
print(lista)
print(type(lista))

# Tuplas
tupla = ("Leviathan", "Xasthur", "Shining", "Lifelover")
print(tupla)
print(tupla[1]) # Acceso
tupla = tuple(sorted(tupla)) # Ordenación
print(tupla)
print(type(tupla))

