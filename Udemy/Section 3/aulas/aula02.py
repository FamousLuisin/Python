# f-string ou formatação de string
print("F-STRINGS")
nome = "Luís Filipe"
altura = 1.80

string_1 = f"{nome} tem {altura:.2f} de altura"

print(string_1)

variavel = "ABCD"
print(f"{variavel:.>10}")
print(f"{variavel:.<10}")
print(f"{variavel:.^10}")


# format
print("\nFORMAT")
string_2 = "{n} tem {a:.2f} de altura".format(n=nome, a=altura)
string_3 = "{n} tem {a:.2f} de altura"

print(string_2)
print(string_3.format(n=nome, a=altura))

# interpolação
print("\nINTERPOLAÇÃO")
nome = "Luis"
preco = 195.352
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)

# fatiamento
print("\nFATIAMENTO")

string_4 = "yamete kudasai"
string_4_fatiada = string_4[1:13:2]
print(f"String: {string_4}\nFatiada: {string_4_fatiada}")