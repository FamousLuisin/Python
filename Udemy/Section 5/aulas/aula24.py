# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...

class MyContextManager:

    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    # O enter é na hora de entrar no with
    def __enter__(self):
        print('Abrindo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    # O exit é na hora de sair do with
    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando')
        self._arquivo.close()

        # Minha excessão
        # raise ConnectionError('Não deu para conectar')

        # Adicionar Notas (Interessante)
        # exception_.add_note('Minha nota')

        # print(class_exception)
        # print(exception_)
        # print(traceback_)

        # Tratei a excessão (Erro passar silenciosamente)
        # return True 
        

caminho = 'C:\\Users\\lufim\\Documents\\GitHub\\Python\\Udemy\\Section 5\\aulas\\aula24\\teste.txt'
instancia = MyContextManager(caminho, 'w')

# O retorno do Enter vai para a variavel algo
# Tudo q tenha o conceito de abrir e fechar, conectar e desconectar, agarra e liberar
with instancia as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('with', arquivo)