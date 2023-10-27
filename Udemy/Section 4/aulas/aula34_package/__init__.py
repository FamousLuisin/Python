# No caso do modulo init é permitido fazer um import *
# em outros e qualquer caso não é uma boa pratica
from .modulo import *
from .novo_modulo import *

print('package importado com sucesso!')

def dobra(x):
    return x * 2