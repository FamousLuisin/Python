def éprimo(numero):
  verificar = divisor = 0

  while divisor < numero:
    divisor = divisor + 1

    if numero % divisor == 0:
      verificar = verificar + 1
    
  if verificar == 2:
    return True
  
  else: 
    return False


def maior_primo(numero):
  maior = 2

  while numero > 2:
    if éprimo(numero):
      maior = numero
      return maior

    else:
      numero = numero - 1



"""def main():
  numero = int(input("Digite um numero: "))
  return maior_primo(numero)"""
