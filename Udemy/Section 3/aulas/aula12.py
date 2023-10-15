frase = "    Olha só       ,       ele é gay    "
# Split separa as palavras ou frases
lista_palavras = frase.split(",") # Se não colocar nada separa pelo espaço em branco

lista_frases = []

for i, frases in enumerate(lista_palavras):
    # strip corta todos os espaços no inicio e no final
    lista_frases.append(lista_palavras[i].strip())

print(frase)
print(lista_palavras)
print(lista_frases)

# Join serve para univer por meio de um caracter ou nenhum os elementos de uma lista ou frases
frase_unidas = "-".join(lista_frases)
print(frase_unidas)