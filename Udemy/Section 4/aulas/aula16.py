# função lambda em python
# função como outro qualquer
# anonima
# contem apenas uma linha

lista = [7, 5, 9, 1, 2, 4, 3]
lista.sort(reverse=True) # metodo para ordenar lista (reverse True muda a ordem)
sorted(lista) # função para ordenar lista
print(lista)


lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir(lista):
    for item in lista:
        print(item)

def ordena_nome(item):
    return item['nome'] # Aqui esta retornando um item que o python saiba como ordenar

# Quando o python for executar o .sort (ordenação) ele vai passar a função e o item que ele ta checanto
# Depois a gente fala oq ele vai usar como meio de ordenação (nesse caso vai ser o 'nome')
# lista.sort(key=ordena_nome) # Tem que passar uma definição de função (function)

# Usando lambda
lista.sort(key=lambda item: item['sobrenome'])

# Usando sorted
lista_nome = sorted(lista, key=lambda item: item['nome'])
lista_sobrenome = sorted(lista, key=lambda item: item['sobrenome'])

print()
print("Lista.sort")
exibir(lista)
print()
print("lista ordenada por nome: sorted")
exibir(lista_nome)
print()
print("lista ordenada por sobrenome: sorted")
exibir(lista_sobrenome)

