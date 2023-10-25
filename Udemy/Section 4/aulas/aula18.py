a, b = 1, 2 # Desempacotar
a, b = 1, 2 # inverter

pessoa = {
    'nome': 'Noki',
    'sobrenome': 'Flinston'    
}

# a, b = pessoa # Desempacotar chaves
# print(a, b)

# print()
# a, b = pessoa.values() # Desempacotar valores
# print(a, b)

# print()
# a, b = pessoa.items() # Desempacotar tuplas (chave, valor)
# print(a, b)

# print()
# (a1, a2), (b1, b2) = pessoa.items() # Desempacotamento internos (Desempacota as tuplas geradas)
# print(a1, a2)
# print(b1, b2)

# print()
# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Noki',
    'sobrenome': 'Flinston'    
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.75
}

pessoa_completa = {**pessoa, **dados_pessoa} # Fomar simples de desempacotar dicionarios usa (**)

print(pessoa_completa)

# args (argumentos não nomeados) e kwargs
# kwargs = keyword argumentos (argumentos nomeados)
# Empacota em formato de dicionarios
def mostrar_argumentos_nomeados(*args, **kwargs): 
    print("===NOMEADOS===")
    for chave, valor in kwargs.items():
        print(chave, valor)
    
    print("===NÃO NOMEADOS===")
    print(args)

# Exemplo de empacotamento 
# mostrar_argumentos_nomeados('YAMETE', 'KUDASAI', nome='Mike', sexualidade='GAY')

# Desempacotar a pessoacompleta e entregar como argumentos nomeados
mostrar_argumentos_nomeados(**pessoa_completa) 