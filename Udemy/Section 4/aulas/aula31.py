# raise vai devolver o erro normal
# ele é usado para caso voce queira tratar algo antes de lançar o erro
# erros são legais
def erro_dividir(y):
    if y == 0:
        raise ZeroDivisionError('numero inválido')
    return True

def erro_tipo(x):
    tipo = type(x)
    if not isinstance(x, (float, int)):
        raise TypeError(
            f'"{x}" deve ser int ou float.'
            f'tipo enviado: "{tipo.__name__}"'
        )

def divide (x, y): # função usada para estudos, caso queira tratar erros deve se criar uma funçao propria
    
    erro_tipo(x)
    erro_dividir(y)
    
    return x / y

print(divide('10', 1))