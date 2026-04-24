def vocales(texto):
    letras_vocales = "aeiouAEIOU"
    contador = 0
    for i in texto:
        if i in letras_vocales:
            contador += 1
    return contador

texto = input("Ingrese un texto: ")
print(f"El número de vocales en su texto es: {vocales(texto)}")
    