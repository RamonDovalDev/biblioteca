"""
Crea un programa en Python que simule el sistema de gestión de una biblioteca utilizando una lista de diccionarios como estructura de datos principal. Cada libro debe almacenar su título, autor, ISBN y estado de disponibilidad.
El programa debe funcionar mediante un menú interactivo en consola con las siguientes opciones:

Agregar libro — registrar un nuevo libro solicitando sus datos al usuario.
Prestar libro — marcar un libro como no disponible buscándolo por ISBN, validando que esté disponible.
Devolver libro — marcar un libro como disponible nuevamente, validando que esté prestado.
Mostrar todos los libros — listar todos los libros registrados con su estado actual.
Buscar libro por ISBN — localizar y mostrar un libro específico.
Salir — finalizar el programa.

Tras cada acción, el sistema debe preguntar al usuario si desea realizar otra operación. El programa debe gestionar correctamente los casos en que no se encuentre un libro o este no esté disponible para la operación solicitada.
"""

# Lista que almacenará los libros de la biblioteca
biblioteca = []

def agregar_libro():
    """ Función para agregar un nuevo libro a la biblioteca """
    titulo = input("Título: ")
    autor = input ("Autor: ")
    isbn = input("ISBN: ")

    libro = {
       "Título": titulo,
       "Autor": autor,
       "ISBN": isbn, 
       "Disponible": True
    }

    biblioteca.append(libro)

    print("¡Libro añadido correctamente")

def prestar_libro():
    """Presta un libro si está disponible"""
    isbn = input("Ingresa el ISBN del libro a prestar: ")

    for libro in biblioteca:
        if libro["ISBN"] == isbn:
            if libro["Disponible"]:
                libro["Disponible"] = False
                print("✅ Libro prestado con éxito")
            else:
                print("❌ El libro ya está prestado")
            return

    print("❌ No se encontró ningún libro con ese ISBN")

def devolver_libro():
    isbn = input("Ingresa el ISBN del libro a devolver: ")

    for libro in biblioteca:
        if libro["ISBN"] == isbn:
            if not libro["Disponible"]:
                libro["Disponible"] = True
                print("✅ Libro devuelto con éxito")
            else:
                print("❌ El libro ya está disponible")
            return

    print("❌ No se encontró ningún libro con ese ISBN")

def mostrar_libros():
    """ Función para mostrar todoz los libros de la biblioteca """
    if not biblioteca:
        print("📚 No hay libros en la biblioteca.")
        return
    
    print("Libros de la biblioteca:")
    for libro in biblioteca:
        estado = "Sí" if libro["Disponible"] else "No"
        print(f"- {libro["Título"]} ({libro['Autor']}) - ISBN: {libro['ISBN']} - Disponible: {estado}")


def buscar_libro_por_isbn():
    isbn = input("Ingresa el ISBN del libro a prestar: ")
    for libro in biblioteca:
        if libro['ISBN'] == isbn:
            print("\n Libro encontrado:")
            estado = "Sí" if libro["Disponible"] else "No"
            print(f"\n✅ Libro encontrado:")
            print(f"- {libro['Título']} ({libro['Autor']}) - ISBN: {libro['ISBN']} - Disponible: {estado}")
            return


def mostrar_menu():
    """ Función para mostrar el menú interactivo y gestionar las opciones """
    while True:
        print("\n" + "=" * 50)
        print("   SISTEMA DE GESTIÓN DE BIBLIOTECA")
        print("="*50)
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar todos los libros")
        print("5. Buscar libro por el ISBN")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            prestar_libro()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            mostrar_libros()
        elif opcion == "5":
            buscar_libro_por_isbn()
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta la próxima!")
            break
        else: 
            print("Opción inválida. Por favor, elige una opción entre 1 y 6.")

        # Preguntar al usuario si desea realizasr otra acción
        if opcion != "6":
            respuesta = input("\n¿Deseas realizar otra acción? (s/n): ").lower()
            if respuesta != "s":
                print("👋 Gracias por usar el sistema. ¡Hasta luego!")
                break
    

if __name__ == "__main__":
    mostrar_menu()


