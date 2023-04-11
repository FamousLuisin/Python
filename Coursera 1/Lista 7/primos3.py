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

def n_primos():

  numero = int(input("Digite um numero: "))

  num = 1


  while num < numero:
    
    num += 1

    if primo(num):
      print(num, end=", ")

    
n_primos()