numero = input("Vou dobrar o numero que você digitar: ")

try:
    numero_float = float(numero)
    print(f"o dobro de {numero_float} é {numero_float * 2}")
except:
    print(f"Isso não é um numero")