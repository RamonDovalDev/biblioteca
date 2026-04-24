"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""

print("=== Verificación de edad ===\n")

# Buble principal
while True:
    try:
        age = int(input("Introduce tu edad: "))
        if age >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")

    except ValueError:
        print("Por favor, introduce un número válido")
        continue # Volver a preguntar la edad

    # Pregunta si desea continuar
    while True:
        respuesta = input("¿Quieres intentarlo otra vez? (s/n): ").strip().lower()
        if respuesta in ['s', 'sí', 'si']:
            print("-" * 30)
            break # Sale del buble interno y vuelve a preguntar edad
        elif respuesta in ['no', 'n']:
            print("Gracias por usar el programa de verificación de edad")
            exit()
        else:
            print("Por favor, responde solo con 's' o 'n'.\n")