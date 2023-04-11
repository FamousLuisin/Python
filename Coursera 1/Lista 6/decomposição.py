def main():
  
  num = int(input("Digite um numero: "))
  divisor = 2
  
  while num > 1:
    
    contador = 0
   
    while num % divisor == 0:
      num = num / divisor
      contador+= 1
      
    if contador > 0:
      print("{}^{}" .format(divisor, contador), end=" ")
    
    divisor += 1


main()
      