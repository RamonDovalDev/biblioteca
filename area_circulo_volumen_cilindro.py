def area_circulo(radio):
    pi = 3.1416
    return pi * radio ** 2

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

print(area_circulo(5))
print(volumen_cilindro(5, 10))