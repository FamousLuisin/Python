numero = int(input("Digite um numero: "))

primo = 0
divisor = 1

while divisor <= numero:
  
  if numero % divisor == 0:
    primo = primo + 1
  
  divisor = divisor + 1

if primo > 2:
  print("não primo")

else:
  print("primo")