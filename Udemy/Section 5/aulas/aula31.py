# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
#
# Usar onde existe um grupo de coisas
import enum

# A enumeração começa do 0
# Direcoes = enum.Enum('Direções', ['ESQUERDA', 'DIREITA'])

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    CIMA = enum.auto()
    BAIXO = enum.auto()

# Trazer membro inteiro
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
# Pegar Numero e Valor
print(Direcoes(1).name, Direcoes.ESQUERDA.value)

print()


def mover(direcao: Direcoes):
    # Se a direção não fizer parte da classe Direcoes
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')

print(type(Direcoes))
print(type(Direcoes.ESQUERDA))

print()

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.CIMA)
mover(Direcoes.BAIXO)
