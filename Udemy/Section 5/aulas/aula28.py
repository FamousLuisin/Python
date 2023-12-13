# Classes decoradoras (Decorator classes)

class Multiplicar_:
    # A classe vai receber a função como parametro no init
    def __init__(self, func):
        self.func = func
        self._multiplicar = 10

    # O call vai receber os parametros da função chamada
    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado * self._multiplicar
        


class Multiplicar:
    # A classe ta recendo parametros ja passados (Multiplicador)
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    # A função nesse caso será passada no call
    # Já que ele ta usando o retorno
    def __call__(self, func):
        # Adiar resultado da função
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna

# Forma um sem chamar inicializar o __init__
# A classe vai pegar a função como parametro
# @Multiplicar_

# Chamando a função __init__
# Nesse caso tera que passar os parametros dentro da classe
# Nesse caso o multiplicador
# Mesmo que Multiplicar()() > callabel (ta chamando a instancia para executar)
@Multiplicar(2) 
def soma(x, y):
    return x + y

dois_mais_quatro = soma(2, 8)
print(dois_mais_quatro)