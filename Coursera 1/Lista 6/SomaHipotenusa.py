def é_hipotenusa(n):
  i = j = 1
  while i <= n:
   
    while j <= n:
      if (n ** 2) == (i ** 2 + j ** 2):
        return True
      j += 1
    
    j = 1
    i += 1

  return False  




def soma_hipotenusas(n):
  soma = 0
  while n > 0:
    
    if é_hipotenusa(n):
      soma = soma + n

    n = n - 1
  
  return soma
