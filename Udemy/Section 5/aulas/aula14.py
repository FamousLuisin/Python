class MinhaString(str):
    def upper(self):
        print('Chamou UPPER')
        # super() > ele retornar o que a classe pai retornaria
        # super(MinhaString, self) > ele chama dessa maneira
        return super().upper()


class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    # Não me importo com oq estou recebendo vou passar para cima(*args, **kwargs)
    # Mas quero executar algo sempre que o __init__ da classe C for usado
    def __init__(self, *args, **kwargs):
        # Comando a ser usado
        print('EI, burlei o sistema.')
        # Chamando os __init__ de cima para receber os valores entregues
        # aqui esta descompactando o args
        super().__init__(*args, **kwargs)
        # B.__init__(self, *args, **kwargs) > Mesca coisa do super
        

    def metodo(self):
        # super().metodo()  # vai ir em B
        # super(B, self).metodo()  # vai ir em A
        # super(A, self).metodo()  # vai ir em object
        A.metodo(self)
        B.metodo(self)
        print('C')


# print(C.mro())
# print(B.mro())
# print(A.mro())

c = C('Atributo', 'Qualquer')
print(c.atributo)
print(c.outra_coisa)
c.metodo()


# string = MinhaString('Luis')
# print(string.upper())