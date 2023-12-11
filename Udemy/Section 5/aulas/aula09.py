# Encapsulamento: (Modificar o acesso: Public, Protected, Private)
# Python não tem modificadores de acesso
# Mas tem convenções:
#   Sem underline = public
#   Um underline = Protected (Não DEVE ser usado fora das classes e subclasses)
#   Dois underline = Private (Só DEVE ser usado na classe em que foi criado - 'name mangling')

class Foo:
    def __init__(self):
        self.public = 'Atributo Publico'
        self._protected = 'Atributo Protegido'
        self.__private = 'Atributo Privado'

    def metodo_public(self):
        print('Publico')
        self._metodo_protected()
        self.__metodo_private()
        return 'Metodo Publico'
    
    def _metodo_protected(self):
        print('Protected')
        self.__metodo_private()
        return 'Metodo Protegido'
    
    def __metodo_private(self):
        print('Privado')
        return 'Metodo Privado'
    
obj = Foo()
# print(obj.public)

obj.metodo_public()