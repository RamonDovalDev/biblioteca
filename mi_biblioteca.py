"""
/*
 * EJERCICIO:
 * Crea un programa que gestione una pequeña biblioteca personal.
 *
 * Datos iniciales:
 * La biblioteca tiene estos libros ya registrados (usa un diccionario):
 *   - "El Quijote":        autor: "Cervantes",  año: 1605, disponible: True
 *   - "1984":              autor: "Orwell",      año: 1949, disponible: True
 *   - "Dune":              autor: "Herbert",     año: 1965, disponible: False
 *
 * El programa debe ofrecer un menú con estas opciones:
 *   1. Mostrar todos los libros y su estado
 *   2. Buscar un libro por título
 *   3. Añadir un nuevo libro
 *   4. Prestar un libro (marcarlo como no disponible)
 *   5. Devolver un libro (marcarlo como disponible)
 *   6. Mostrar solo los libros disponibles
 *   7. Salir
 *
 * Requisitos:
 * - Los datos de cada libro se guardan en una TUPLA
 *   (autor, año, disponible)
 * - Todos los libros se guardan en un DICCIONARIO
 *   donde la clave es el título
 * - El historial de operaciones realizadas
 *   (prestar, devolver, añadir) se guarda en una LISTA
 * - Al salir, mostrar el historial completo de operaciones
 */
"""
import time

# === DATOS INICIALES ===
biblioteca = {
    "El Quijote": ("Cervantes", 1605, True),
    "1984": ("Orwell", 1949, True),
    "Dune": ("Herbert", 1965, False)
}

historial = []

# === FUNCIONES AUXILIARES ===
def mostrar_libros(libros=None):
    """Muestra los libros. Si no se pasa nada, muestra todos."""
    if libros is None:
        libros = biblioteca
    
    if not libros:
        print("📚 No hay libros registrados.")
        return
    
    print(f"\n{'Título':<30} {'Autor':<20} {'Año':<6} {'Estado'}")
    print("-" * 70)
    # Estado de los libros
    for titulo, (autor, año, disponible) in libros.items():
        estado = "✅ Disponible" if disponible else "❌ Prestado"
        print(f"{titulo:<30} {autor:<20} {año:<6} {estado}")

def buscar_libro():
    titulo = input("\nIntroduce el título del libro a buscar: ").strip()
    if titulo in biblioteca:
        autor, año, disponible = biblioteca[titulo]
        estado = "✅ Disponible" if disponible else "❌ Prestado"
        print(f"\n✅ Libro encontrado:")
        print(f"Título: {titulo}")
        print(f"Autor: {autor}")
        print(f"Año: {año}")
        print(f"Estado: {estado}")
    else:
        print("❌ Libro no encontrado")

def agregar_libro():
    titulo = input("\nTítulo del nuevo libro: ").strip()
    if titulo in biblioteca:
        print("⚠️ Este libro ya se encuentra en la biblioteca")
        return
    
    autor = input("Autor: ").strip()
    while True:
        try:
            año = int(input("Año de pubblicación: "))
            break
        except ValueError:
            print("❌ Por favor, introduce un año válido.")

    biblioteca[titulo] = (autor, año, True)
    historial.append(f"📕 Añadido: '{titulo}' de {autor} ({año})")
    print("✅ Libro añadido correctamente")

def prestar_libro():
    titulo = input("\nTítulo del libro a prestar: ").strip()
    if titulo not in biblioteca:
        print("❌ Libro no encontrado.")
        return
    
    autor, año, disponible = biblioteca[titulo]
    if not disponible:
        print("❌ Este libro ya está prestado.")
        return
    
    # Convertimos la tupla a lista para modificarla
    libro_lista = list(biblioteca[titulo])
    libro_lista[2] = False
    biblioteca[titulo] = tuple(libro_lista)
    
    historial.append(f"📤 Prestado: '{titulo}'")
    print(f"✅ Libro '{titulo}' prestado correctamente.")

def devolver_libro():
    titulo = input("\nTítulo del libro a devolver: ").strip()
    if titulo not in biblioteca:
        print("❌ Libro no encontrado")
        return

    autor, año, disponible = biblioteca[titulo]
    if disponible:
        print("❌ Este libro ya está disponible.")
        return
    
    libro_lista = list(biblioteca[titulo])
    libro_lista[2] = True
    biblioteca[titulo] = tuple(libro_lista)

    historial.append(f"📥 Devuelto: '{titulo}'")
    print(f"✅ Libro '{titulo}' devuelto correctamente.")

def mostrar_disponibles():
    disponibles = {k: v for k, v in biblioteca.items() if v[2]}
    mostrar_libros(disponibles)


# === MENÚ PRINCIPAL ===
print("📖 ¡BIENVENIDO A TU BIBLIOTECA PERSONAL 📖")

while True:
    print('\n' + "-"*50)
    print("1. Mostrar todos los libros")
    print("2. Buscar libro por título")
    print("3. Añadir nuevo libro")
    print("4. Prestar un libro")
    print("5. Devolver un libro")
    print("6. Mostrar solo libros disponibles")
    print("7. Salir")
    print("="*50)

    opcion = input("\nElige una opción (1-7): ")

    match opcion:
        case "1":
            mostrar_libros()
        case "2":
            buscar_libro()
        case "3":
            agregar_libro()
        case "4":
            prestar_libro()
        case "5":
            devolver_libro()
        case "6":
            mostrar_disponibles()
        case "7":
            print("Saliendo de la biblioteca...")
            break
        case _:
            print("❌ Opción no válida. Intenta del 1 al 7.")

    # Pequeña pausa para mejor experiencia de usuario 
    if opcion != "7":
        time.sleep(0.7)

# === HISTORIAL COMPLETO DE OPERACIONES ===
print("\n" + "="*60)
print("📜 HISTORIAL COMPLETO DE OPERACIONES")
print("="*60)

if historial:
    for i, operacion in enumerate(historial, 1):
        print(f"{i:2d}. {operacion}")
else:
    print("No se realizó ninguna operación")

print("="*60)
print("¡Gracias por usar tu biblioteca personal!")