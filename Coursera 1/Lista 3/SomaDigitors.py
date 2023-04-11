numero = int(input("Digite um numero: "))

soma = numero % 10

while numero // 10 != 0:
  numero = numero // 10
  soma = soma + (numero % 10)

print(soma)