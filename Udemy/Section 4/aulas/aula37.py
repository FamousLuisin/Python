# Essa é uma fabrica de decoradores, ela gera varios decoradores conforme necessario
# Usada para pegar os parametros do decorador
def fabrica_de_decoradores(x=None, y=None, z=None): 
    
    # Fabrica de funções ou decorador (Deve sempre receber uma função)
    def fabrica_de_funcoes(func): 
        print('Decoradora 1')

        # Função aninhada mais interna irá subistituir a função real(nesse caso a soma)
        def aninhada(*args, **kwargs): 
            print('Parametros: {}, {}, {}'.format(x, y, z))
            print('aninhada')
            res = func(*args, **kwargs)
            return res + 20
        
        return aninhada
    
    return fabrica_de_funcoes

# Ela já é executada no inicio do codigo e guarda a função no escopo da decoradora caso não use "()"
@fabrica_de_decoradores(1, 3, 5)
def soma(x, y):
    return x + y

decoradora = fabrica_de_decoradores()

multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)