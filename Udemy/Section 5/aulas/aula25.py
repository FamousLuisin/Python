# Usar função decorada no context Manager
# Criando e usando gerenciadores de context

from contextlib import contextmanager

# Função Generator
@contextmanager
def MyOpen(caminho, modo):
    # Tratar excessão
    try:
        print('Abrindo')
        arquivo = open(caminho, modo, encoding='utf8')
        # Duas ações abir e fechar
        # yiedl faz se tornar um generator q pode retornar mais de uma coisa em tempos diferentes
        yield arquivo
    except Exception as e:
        print('Ocorreu Erro', e)
    finally:
        print('Fechando o aruqivo')
        arquivo.close()


caminho = 'C:\\Users\\lufim\\Documents\\GitHub\\Python\\Udemy\\Section 5\\aulas\\aula24\\teste.txt'

with MyOpen(caminho, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('with', arquivo)