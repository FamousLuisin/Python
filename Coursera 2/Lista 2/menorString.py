def primeiro_lex(lista):
  menor = lista[0]
  for string in lista:
    if string < menor:
      menor = string
  return menor

