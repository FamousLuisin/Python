# arquivo main

# importar moudlos e package
# package é o lugar para organizar os arquivos / modulos

import aula34_package # importando apenas o package
import aula34_package.modulo as aula
from aula34_package import modulo
from aula34_package.modulo import soma, saudacao

print('=====Modulo=====')
print(aula.soma(3, 4))
print(modulo.soma(5, 5))
print(soma(10, 10))

print()

# Saudação vinda do "novo_modulo" que veio junto com o "modulo"
print('=====Novo_Modulo=====')
saudacao()

print()

# O package "engana" o python, já que caso importe apenas o package
# o __init__ ainda será inicializado e com isso os comandos dele tbm
print('=====__init__=====')
print(aula34_package.dobra(2))
# acessando a função do "modulo" a partir do package
print(aula34_package.soma(7, 14))