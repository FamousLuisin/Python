# aquivo modulo, dentro do package
# package é o lugar para organizar os arquivos / modulos

# O all aqui está dizendo que quando alguem importa tudo usando "*"
# ele irá devolver apenas o que esta dentro do __all__
__all__ = [
    'string'
]

string = 'Noki'

from aula34_package.novo_modulo import saudacao

def soma(x, y):
    return x + y