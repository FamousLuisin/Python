# Manipulando dicionarios

pessoa = {}

chave_nome = 'nome' # criar

pessoa[chave_nome] = 'Noki'
pessoa['sobrenome'] = 'Flinston'

print(pessoa[chave_nome]) #acessar
print(pessoa)

del pessoa['sobrenome'] # Deletar

print(pessoa)

# Verificar se existe uma chave especifica

if pessoa.get('sobrenome') is not None: 
    print("Existe")
    print(pessoa['sobrenome'])
else:
    print("Não existe")