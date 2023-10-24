# Exemplo de exercicio com set

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Pabarens!')
        break

    print(letras)