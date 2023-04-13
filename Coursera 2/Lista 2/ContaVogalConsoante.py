def  conta_letras(frase, contar="vogais"):
  frase = frase.upper()
  cont = 0
  if contar == "vogais":
    for vogal in range(len(frase)):
      if frase[vogal] == "A" or frase[vogal] == "E" or frase[vogal] == "I" or frase[vogal] == "O" or frase[vogal] == "U":
        cont += 1
  
  else:
    for vogal in range(len(frase)):
      if frase[vogal] != "A" and frase[vogal] != "E" and frase[vogal] != "I" and frase[vogal] != "O" and frase[vogal] != "U":
        cont += 1
    cont = cont - frase.count(" ")
  
  return cont



