numero = int(input("Digite um numero inteiro: "))
numeroAnterior = numero % 10

adjacente = False

while numero  // 10 != 0 and not adjacente:
  numero = numero // 10
  
  if numeroAnterior == numero % 10:
    adjacente = True
  
  numeroAnterior = numero % 10

if adjacente:
  print("sim")

else:
  print("não")
