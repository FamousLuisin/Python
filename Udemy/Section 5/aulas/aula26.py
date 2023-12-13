# Funções decoradoras e decoradores com classes
# Class sem repr so mostra o endereço de memória

def adicionar_repr(cls):
    # Caso queira tbm pode adicionar essa função fora da função principal
    def meu_repr(self):
        # Nome do objeto
        class_name = self.__class__.__name__
        # __dict__ torna o objeto em dicionario
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    # Adicionar um repr dentro da classe
    cls.__repr__ = meu_repr
    return cls


# Método ainda assim é passado para a função
# Dessa forma so precisamos retornar o método
def meu_nome(metodo):
    def interno(self, *args, **kwargs):
        # Retorno do método
        # Deve tbm passar o self e o args/kwargs para dentro do método
        # Dessa forma não haverá erros
        resultado = metodo(self, *args, **kwargs)
        print(metodo.__name__)
        if 'Terra' in resultado:
            return 'Você esta em casa'
        return resultado
    return interno

# Aqui ele ja está mandando a classe como parametro para a função adicionar_repr
# E ela ja esta retornando a classe com o repr
# Melhor jeito de se fazer
@adicionar_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

    @meu_nome
    def falar_nome_time(self):
        return f'O Time é {self.nome}'

@adicionar_repr
class Planeta:
    def __init__(self, nome):
        self. nome = nome

    # Decorar um método
    @meu_nome
    def falar_nome_planeta(self):
        return f'O planeta é {self.nome}'


# Aqui ele esta adicionando o repr dentro da classe
# E lançando dnv a classe
# Time = adicionar_repr(Time)   
# Planeta = adicionar_repr(Planeta) 


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Mater')

print('='*11+'repr'+'='*11)
print(brasil)
print(portugal)
print(terra)
print(marte)
print('='*26)

print()

print('='*10+'Planet'+'='*10)
print(terra.falar_nome_planeta())
print(marte.falar_nome_planeta())
print('='*26)

print()

print('='*11+'Time'+'='*11)
print(brasil.falar_nome_time())
print(portugal.falar_nome_time())
print('='*26)