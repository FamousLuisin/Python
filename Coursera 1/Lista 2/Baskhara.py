#import serve para importar um module de funções externo
import math

#ax² + bx + c = 0

a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))

delta = b ** 2 - 4 * a * c

#if se a condição for verdadeira ele segue o bloco de comnados a baixo
if delta < 0:
  print("esta equação não possui raízes reais")

#else se a condição não for verdadeira ele segue o bloco de comnados a baixo
else:
  raizDelta = math.sqrt(delta)

  if delta == 0:
    raiz = (-b + raizDelta) / (2 * a)
    print("a raiz desta equação é", raiz)
  
  else:
    raiz1 = (-b + raizDelta) / (2 * a)
    raiz2 = (-b - raizDelta) / (2 * a)
    if raiz1 < raiz2:
      print("as raízes da equação são {} e {}" .format(raiz1, raiz2))

    else:
      print("as raízes da equação são {} e {}" .format(raiz2, raiz1))

