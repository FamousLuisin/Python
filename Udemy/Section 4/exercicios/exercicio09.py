# Clousere (adiar execução)
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_func(funcao, x):
    def executar(y):
        return funcao(x, y)
    return executar

# exemplo um
soma_cinco = criar_func(soma, 5)
multiplica_dez = criar_func(multiplica, 10)

print(soma_cinco(10))
print(multiplica_dez(10))

