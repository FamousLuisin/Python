def fatorial(num):
  
  fatorial = 1
  
  while num > 0:
    fatorial = fatorial * num
    num = num - 1
  
  return fatorial


def main():
  
  num = int(input("Informe um valor: "))
  
  while num >= 0:

    print(fatorial(num))
    num = int(input("Informe um valor: "))

main()