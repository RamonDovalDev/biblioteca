# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un 
# alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, 
# la nota media, la nota más alta que ha sacado y la menor.

import time

print("📊 CALCULADORA DE NOTAS - 5 calificaciones\n")

while True:                                 # Bucle principal para repetir el programa
    notas = []                              # Lista para guardar las 5 notas
    
    print("Introduce las 5 notas del alumno (entre 0 y 10):\n")
    
    # ====================== LECTURA DE LAS 5 NOTAS ======================
    for i in range(1, 6):
        while True:                         # Bucle de validación
            try:
                nota = float(input(f"Nota {i}: "))
                
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("❌ Error: La nota debe estar entre 0 y 10.")
            except ValueError:
                print("❌ Error: Por favor introduce un número válido.")
    
    # ====================== PROCESAMIENTO ======================
    nota_media = sum(notas) / 5
    nota_maxima = max(notas)
    nota_minima = min(notas)
    
    # ====================== MOSTRAR RESULTADOS ======================
    print("\n" + "="*40)
    print("📋 RESULTADOS")
    print("="*40)
    
    # Mostrar todas las notas
    print("Notas introducidas:", end=" ")
    for nota in notas:
        print(f"{nota:.1f}", end="  ")
    
    print(f"\n\nNota media     : {nota_media:.2f}")
    print(f"Nota más alta  : {nota_maxima:.1f}")
    print(f"Nota más baja  : {nota_minima:.1f}")
    print("="*40)
    
    # ====================== REPETIR O SALIR ======================
    while True:
        respuesta = input("\n¿Quieres calcular las notas de otro alumno? (s/n): ").strip().lower()
        
        if respuesta in ["s", "si", "sí", "y", "yes"]:
            print("\n" + "-"*50)
            break
        elif respuesta in ["n", "no"]:
            print("\n¡Gracias por usar el programa! 👋")
            exit()                    # Salir del programa
        else:
            print("Por favor responde con 's' o 'n'.")



