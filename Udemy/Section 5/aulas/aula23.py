# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

class A:
    # new é chamado antes do init (responsavel por cirar a instancia)
    # Não é muito usado / Necessario
    def __new__(cls, *agrs, **kwargs):
        print('Antes de criar a instancia')
        # Criar a insatncia da classe
        instancia =super().__new__(cls)
        print('Depois de criar a instancia')
        # retorno da instancia para o __init__
        return  instancia

    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return 'A()'
    

a = A(777)
print(a.x)
