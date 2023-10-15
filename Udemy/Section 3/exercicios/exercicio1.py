# Exercicio 1
string = "Luís"

tamanho_string = len(string)
indice = 0
nova_string = "*"

while indice < tamanho_string:
    nova_string += f"{string[indice]}*"
    indice += 1

print(nova_string)