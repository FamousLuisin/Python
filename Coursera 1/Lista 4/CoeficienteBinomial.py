def fatorial(x):
  fat = 1
  while x > 0:
    fat = fat * x
    x = x - 1
  
  return fat

def main():
  n = int(input("Digite o valor de n: "))
  k = int(input("Digite o valor de k: "))

  Coeficiente = fatorial(n) / (fatorial(k) * fatorial(n - k))

  return Coeficiente


print(main())
