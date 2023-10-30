# Se não passar um parametro mutavel, ele sempre irá usar um argumento ja passado 
# nesse caso uma lista
# MELHOR FORMA de resolver é não passar valores mutaveis para parametros padrões
# Podemos colocar lista=None ao inves de lista=[]
def add_clientes(nome, lista=None):
    # Dessa forma evita o erro
    # esse codigo será executado criando uma nova lista sem ter preocupações com chamadas antigas
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

# Uma forma de resolve é passando uma lista já de inicio
lista_clientes = []

clientes_x = add_clientes('Noki', lista_clientes)
add_clientes('Flinston', clientes_x)
print(clientes_x)

# MELHOR FORMA
clientes_y = add_clientes('Jhonson')
add_clientes('Frisus', clientes_y)
print(clientes_y)


