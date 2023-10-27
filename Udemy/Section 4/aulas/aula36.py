# Função decoradora 
# (syntax sugar) > possui um recurso que facilita o uso das funções decoradoras
# (uma funçao que recebe como parametro outro função e devolve essa outra função para ser usada)
def criate_function(func):
    # Criar uma função interna para ter uma clousure
    # A função interna não será executada e sim retornada como uma função
    # para ser executada futuramente
    # na execução dessa função podemos por exemplo executar algo antes ou dps do resoltada da func
    def interna(*args, **kwargs):
        print('Vou te decorar') # podemos adcionar coisas antes
        for arg in args:
            is_string(arg) # podemos restringir
        resultado = func(*args, **kwargs)
        resultado += '123' # podemos alterar
        print('Decorada com sucesso:', resultado) # podemos adcionar coisas depois
        return resultado
    
    return interna

# (syntax sugar) > Usar @nome_funçao_decorada em cima da função que deseja usar
# Ele passa automaticamente aquela função, como parametro da função decoradora
@criate_function
def inverte_string(string):
    # A função inverte_string passa a ser a função interna do decorador
    print(inverte_string.__name__)
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

inverter = inverte_string('123')
print(inverter)

# Na mão
# teste_inverter = criate_function(inverte_string)
# invertida = teste_inverter('123')
# print(invertida)

