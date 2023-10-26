import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
lista = [n for n in range(10000)]
generator = (n for n in range(10000)) # Usar () para fazer um generator
# a vantagem da lista é q podemos acessar indice por indice
# sys.getsizeof calcula o peso daquele elemento
print(sys.getsizeof(lista)) # A lista salva todos os valores na memoria
# O generator ele funciona como um iteravel, so mostrando o proximo elemento (mostra um por vez)
# Função que pausa
print(sys.getsizeof(generator))
print(next(generator))
print(next(generator))
print(next(generator))