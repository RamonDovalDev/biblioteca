# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia.
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def count_words(text):
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else: 
            words[i] = 1
    return words

def most_repeated(words):
    max_word = ""
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return (max_word, max_freq)

text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(count_words(text))
print(most_repeated(count_words(text)))

