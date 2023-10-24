# Mais sobre lambda

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

# Aqui já é muito complexo é melhor usa a função
def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = cria_multiplicador(2)
duplica = executa(
        lambda m: lambda n: n * m, 2
    )

print(
    # Lambda de uma linha e simples é muito bom
    'lambda:',
    executa(
        lambda x, y: x + y, 2, 3 # (x, y) = parametros / (x + y) = retorno / (2, 3) = argumento
    ),
    '\nexecuta(soma):',
    executa(soma, 2, 3),
    '\nsoma():',
    soma(2, 3)
)

print(
    'duplciador:', duplica(5)
)

print(
    'Soma:',
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 6, 7
    )
)