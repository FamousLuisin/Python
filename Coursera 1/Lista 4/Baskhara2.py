import math

def delta(a, b, c):
  delta = b ** 2 - (4 * a * c)
  return delta


def raizes(a, b, delta):
  if delta < 0:
    print("Não existe raizes reais")
  
  else:
    raizDelta = math.sqrt(delta)
    
    if delta == 0:
      raiz = (-b + raizDelta) / (2 * a)
      print( "A raiz de delta é:", raiz)
    
    else:
      raiz1 = (-b - raizDelta) / (2 * a)
      raiz2 = (-b + raizDelta) / (2 * a)
      print( "As raizes de delta são: {} e {}" .format(raiz1, raiz2))



def main():
  a = int(input("Informe o valor de a: "))
  b = int(input("Informe o valor de b: "))
  c = int(input("Informe o valor de c: "))

  raizes(a, b, delta(a, b, c))

main()



