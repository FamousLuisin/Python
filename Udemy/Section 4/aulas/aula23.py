# uso com debbuger console
# dir = ver todos os nomes daquele objeto
# hasattr = ver se a string tem um determinado metodo
# getattr = pegar/capturar o metodo de uma função

string ='Noki'
metodo = 'upper'

print("===DIR===")
print(dir(string))

print("\n===HASATTR AND GETATTR===")
if hasattr(string, metodo):
    print('Existe upper aqui')
    print(getattr(string, metodo)())
    print(string.upper())