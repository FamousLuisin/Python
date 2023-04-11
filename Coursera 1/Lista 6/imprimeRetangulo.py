def main():
  largura = int(input("Digite a lergura: "))
  altura = int(input("Digite a altura: "))

  j = i = 0

  while i < altura:
    while j < largura:
      print("#", end="")
      j += 1
    print()
    j = 0
    i += 1

main()