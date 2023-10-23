import os

perguntas = [
    {
        'pergunta': 'Quanto é 2 + 2?',
        'opções': ['1', '2', '3', '4'],
        'resposta': '4',
    },
    {
        'pergunta': 'Quanto é 5 * 5?',
        'opções': ['10', '25', '30', '40'],
        'resposta': '25',
    }
]

acertos = 0

for dicionario in perguntas:
    print(dicionario['pergunta'])
    print('opções:')

    opcoes = dicionario['opções']
    for i, option in enumerate(opcoes):
        print(f'{i}) {option}')
        

    escolha = input('Escolha sua opção: ')


    # try and except
    try:
        escolha = int(escolha)
        if opcoes[escolha] == dicionario['resposta'] and escolha >= 0:
            print("ACERTOU")
            acertos += 1
        else:
            print("ERROU")
    except IndexError:
        print("Opção fora do range")
        print("ERROU")
    except ValueError:
        print("Valor invalido, não é numero inteiro")
        print("ERRO")


    # .isdigit
    # acertou = False
    # escolha_int = None

    # if escolha.isdigit():
    #     escolha_int = int(escolha)

    # if escolha_int is not None:
    #     if escolha_int >= 0 and escolha_int < len(opcoes):
    #         if opcoes[escolha_int] == dicionario['resposta']:
    #             acertou = True

    # print()
    # if acertou:
    #     acertos += 1
    #     print('Acertou 👍')
    # else:
    #     print('Errou ❌')

    print()
    


print("Você acertou", acertos, "perguntas de", len(perguntas))

    