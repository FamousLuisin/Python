def main():
  largura = int(input("Digite a lergura: "))
  altura = int(input("Digite a altura: "))

  j = i = 1

  while i <= altura:
    
    while j <= largura:
      if i == 1 or i == altura or j == 1 or j == largura:
        print("#", end="")
      
      else:
        print(" ", end="")
      j += 1
    
    print()
    j = 1
    i += 1

main()