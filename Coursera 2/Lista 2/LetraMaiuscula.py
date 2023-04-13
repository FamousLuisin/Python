def main():
  texto = str(input("Digite um texto: "))
  return maiusculas(texto)


def maiusculas(texto):
  letras = ""
  for letra in range(len(texto)):
    
    if ord(texto[letra]) >= 65 and ord(texto[letra]) <= 90:
      letras = letras + texto[letra]
  
  return letras

print(main())
