def primo(num):

  if num == 2:
    return True

  divisor = 2
  while num % divisor != 0 and divisor < num/2:
    divisor += 1
  
  if num % divisor == 0:
    return False
  
  else:
    return True


def main():
  num = int(input("Digite um numero: "))

  while num > 0:
    
    if primo(num):
      print("é primo")
    
    else:
      print("não primo")

    num = int(input("Digite um numero: "))

main()