# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html

from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index

    # Chamar um item da lista com colchetes
    def __getitem__(self, index):
        return self._data[index]

    # Atribuir um valor a lista com os colchetes
    def __setitem__(self, index, value):
        self._data[index] = value

    # Retornar um iteravel (No caso aqui é a propria instancia)
    def __iter__(self):
        return self

    # Retornar o proximo valor da lista
    def __next__(self):
        # Lógica de para do next
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Luiz')
    # print(lista[0])
    # print(len(lista))
    for item in lista:
        print(item)
    print('---')
    for item in lista:
        print(item)
    print('---')