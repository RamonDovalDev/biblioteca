# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
while True:
    word = input("Introduce una palabra: ")
    reverse_word = word
    word = list(word)
    reverse_word = list(reverse_word)
    reverse_word.reverse()
    if word == reverse_word:
        print("Es un palíndromo")
    else: 
        print("No es un palíndromo")

    question = input("Deseas continuar?: (s/n)")
    if question.lower() == "n":
        print("¡Gracias por participar!")
        break