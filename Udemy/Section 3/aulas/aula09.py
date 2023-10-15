# Listas são tipos mutáveis
lista_um = ["Luís", 10.5, 10, False]

# Ler toda a lista
lista_dois = [10, 20, 30]
print("Ler toda a lista", lista_dois)

# Ler um valor
print("Ler um valor da lista", lista_dois[0])

# Alterar um valor
lista_dois[0] = 40
print("Alterar um valor", lista_dois)

# Deletar um valor
del lista_dois[0]
print("Deletar um valor", lista_dois)

# Adicionar um valor no final da lista
lista_dois.append(50)
lista_dois.append(60)
lista_dois.append(70)
print("Adicionar um valor", lista_dois)

# Remover o ultimo elemento
# O pop ele remove e entrega o ultimo valor, ou do indice escolhido
valor_removido = lista_dois.pop(2) 
print("Remover ultimo valor", lista_dois, valor_removido)

# Inserir um valor
# O insert primeiro você entrega o indice depois o valor que vai naquele indice
lista_dois.insert(0, 10)
print("Adicionar um valor", lista_dois)

# Apagar tudo de uma lista
lista_dois.clear()
print("Apagar toda a lista", lista_dois)

# Concaternar listas
lista_a = [1, 2, 3]
print("Lista a:", lista_a)
lista_b = [4, 5, 6]
print("Lista a:", lista_a)
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # Não retorna nada

print("Lista a depos do extend:", lista_a)
print("Lista c concatenação entre lista_a e lista_b:", lista_c)

# Copiar lista
lista_a = [1, 2, 3]
lista_b = lista_a.copy()
print("Copiada", lista_a)
print("copia", lista_b)
