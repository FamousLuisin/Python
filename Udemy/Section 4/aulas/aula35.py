# def fora(x):
#     # Variavel livre
#     a = x

#     # Clousere
#     def dentro():
#         print(locals())
#         # print(dentro.__code__.co_freevars)
#         return a
#     return dentro

# variavel = fora(10)
# print(variavel())

def concaternar(string):
    valor_final = string
    

    def interna(string_dois):
        # nonlocal permite alterar variaveis livres
        nonlocal valor_final
        print(valor_final)
        valor_final += string_dois
        return valor_final
    
    return interna

c = concaternar('a')
print(c('b'))
print()
print(c('c'))
print()
print(c('d'))