# Herança Múltipla (TOMAR CUIDADO) - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins (Sempre que possivel usar composição)
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# Problema do Diamante
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar (existem em A, B, C)
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)

class A(object):
    ...
    def falar(self):
        print('A')

class B(A):
    ...
    def falar(self):
        print('B')

class C(A):
    ...
    def falar(self):
        print('C')

class D(B, C):
    ...
    def falar(self):
        print('D')

d = D()
d.falar()

# mro serve para saber a ordem de resolução, 
# no caso a sequencia de busca do programa
print(D.mro())