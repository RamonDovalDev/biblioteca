# Programa interactivo para obtner números factoriales
def factorial(n):
    """Devuelve el facotrial de n, un entero no negativo"""
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")
    if n == 0 or n == 1:
        return 1
    resultado = 1

    # Cáculo del factorial
    for i in range(1, n +1):
        resultado *= i
    return resultado

# Función principal interactiva
def main():
    print("=== Calculadora de Factoriales ===")
    while True:
        try:
            # 1 Pedir al usuario que ingrese un número
            num = int(input("Ingrese un número entero positivo para calcular su factorial: "))
            # 2. Calcular el factorial usando la función definida
            fact = factorial(num)
            print(f"El factorial de {num} es: {fact}\n")
        except ValueError as e:
            if "no está definido" in str(e):
                print("❌ Error:", e)
            else:
                print("❌ Error: Por favor, introduce un número entero válido.")
            print()
            continue # Volver a pedir número

        # 3. Preguntar al usuario si desea continuar
        while True:
            respuesta = input("¿Desea calcular otro número factorial? (s/n): ").strip().lower()
            if respuesta == 's':
                print() # Salto de línea para mejor legibilidad
                break # Salir del bucle de respuesta y volver a pedir número
            elif respuesta == 'n':
                print("¡Gracias por participar! ¡Hasta luego!")
                return # Salir del programa
            else:
                print("Por favor, responda con 's' para sí o 'n' para no.")
                continue # Volver a preguntar

# Ejecutar el programa
if __name__ == "__main__":
    main()