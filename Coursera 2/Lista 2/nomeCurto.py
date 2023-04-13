def menor_nome(lista_nomes):
  menor = lista_nomes[0]
  for nome in lista_nomes:
    if len(nome.strip()) < len(menor):
      menor = nome.strip()
    
  return menor.capitalize()

print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))