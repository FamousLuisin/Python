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

def n_primos(numero):
  cont = 0

  while numero > 1:
    
    if primo(numero):
      cont += 1
    
    numero -= 1
  
  return cont

  