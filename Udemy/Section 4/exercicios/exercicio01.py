# Criar função para multiplicar todos os numeros / argumentos enviados

def multiplica(*args):
    multiplica = 1
    for numero in args:
        multiplica *= numero
    return multiplica

numeros = 2, 5, 10
valor_final = multiplica(*numeros)

print(valor_final)
print(2*5*10)
