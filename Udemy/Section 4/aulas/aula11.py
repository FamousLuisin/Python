pessoa = {
    'nome': 'Noc',
    'sobrenome': 'Flinston',
    'idade': 22
}

print('===get===')
# Pega o que esta armazenado em uma chave
print(pessoa.get('nome')) 
# Caso não exista ele retorna None, ou um valor pré determinado
print(pessoa.get('idade', 'não definida'))

print('\n===pop===')
# Exclui e retorna a chave e o valor da chave exlcuido, nesse caso foi o sobrenome
sobrenome = pessoa.pop('sobrenome')
print(sobrenome)
print(pessoa)

# Exclui e retorna a ultima chave e seu valor
print('\n===popitem===')
ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

print('\n===update===')
# Update você mexe diretamenta na lista
# Primeiro modo
pessoa.update({
    'nome': 'Jhonson', # Alterar valor
    'vulgo': 'ShaCoxudo' # Adicionar chave e valor
})

# Segundo modo
# pessoa.update(nome='Jhonson', vulgo='ShaCoxudo')

# Terceiro modo (pode ser com tuplas tbm)
# lista = [['nome', 'Jhonson'], [ 'vulgo', 'ShaCoxudo']]
# pessoa.update(lista)

print(pessoa)