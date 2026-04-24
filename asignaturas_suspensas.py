# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = ["Matemáticas", "Lengua", "Biología", "Ciencias Sociales", "Religion", "Física y Química", "Educación Física", "Historia"]
suspendidas = []

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}: "))
    if nota < 5:
        suspendidas.append(asignatura)
print(f"Tienes que repetir {suspendidas}")