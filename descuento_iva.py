def aplicar_descuento(precio, descuento):
    return precio - (precio * descuento / 100)

def aplicar_iva(precio, porcentaje):
    return precio + (precio  * porcentaje / 100)

def precio_cesta(cesta, funcion):
    total = 0
    for precio, descuento in cesta.items():
        total += funcion(precio, descuento)
    return total

print("El precio total de la compra tras aplicar descuentos es: ", precio_cesta({1000: 20, 500: 5, 100: 2}, aplicar_descuento))
print("El precio total de la compra tras aplicar el IVA es: ", precio_cesta({1000: 21, 500: 21, 100: 21}, aplicar_iva))