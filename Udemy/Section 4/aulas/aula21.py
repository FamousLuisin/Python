# isinstance - para saber se objeto é de determinado tipo

lista = [
    's', 1, 1.1, True, [0, 1, 2], {'nome': 'Luis'}, {0, 1}, (1, 2)
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        # receber um objeto e um tipo, e verifica se o objeto é daquele tipo
        item.add(5)
        print(item)

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    # Se passar uma tupla, vai ser ou um tipo ou o outro tipo
    elif isinstance(item, (int, float)): # nesse caso é int ou float
        print('NUM')
        print(item, item * 2)

    else:
        print('OUTROS')
        print(item)