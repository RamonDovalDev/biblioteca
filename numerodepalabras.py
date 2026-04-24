# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
def contar_palabras(frase):
    palabras = frase.split()
    longitudes = map(len, palabras)
    return dict(zip(palabras, longitudes))

print(contar_palabras("Me cago en la hostia puta"))
