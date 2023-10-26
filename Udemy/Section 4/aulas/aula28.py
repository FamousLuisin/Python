def gen1():
    print('Começou gen1')
    yield 1
    yield 2
    yield 3
    print('Acabou gen1')

def gen2(gen=None): # ele ta recebendo o nome da função
    print('Começou gen2')
    if gen is not None:
        # aqui esta usando o nome da funçao recebida para usar ela juntando com os "()"
        yield from gen() # Ele vai começar daonde o outro gerador parou
    yield 4
    yield 5
    yield 6
    print('Acabou gen2')

def gen3():
    print('Começou gen3')
    yield 7
    yield 8
    yield 9
    print('Acabou gen3')

# No caso aqui o gen2 iniciar, vai até o yield from gen()
# Que chama o outro gen, enquanto o gen2 fica parado
# Quando o gen() acaba, volta para o gen2()
g1 = gen2(gen1)
g2 = gen2(gen3)
g3 = gen2()

for numero in g1:
    print(numero)

print('==========')

for numero in g2:
    print(numero)

print('==========')

for numero in g3:
    print(numero)
