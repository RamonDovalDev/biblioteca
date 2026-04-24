# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
def factura(cantidad, iva=21):
    return cantidad + (cantidad * iva / 100)

print (factura(1000, 10))
print(factura(1000))