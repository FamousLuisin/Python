numero = int(input("Digite um numero: "))

fatorial = 1

while numero > 0:
  fatorial = fatorial * numero
  numero = numero - 1

print(fatorial)