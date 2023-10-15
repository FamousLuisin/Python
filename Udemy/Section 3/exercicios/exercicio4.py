# FEITO POR MIM

# palavra_secreta = "Yamete"
# palavra_oculta = "*" * len(palavra_secreta)
# palavra_intermediaria = ""

# print(palavra_oculta)

# letra = ""
# tentativas = 0

# while True:
#     tentativa = input("Digite uma letra: ")

#     if len(tentativa) > 1:
#         print("É permitido apenas uma letra")
#         continue

#     tentativas += 1

#     if tentativa in palavra_secreta:
#         palavra_intermediaria = ""
#         for indice in range(len(palavra_secreta)):
#             if palavra_secreta[indice] == tentativa:
#                 palavra_intermediaria += tentativa
#             else:
#                 palavra_intermediaria += palavra_oculta[indice]

#         palavra_oculta = palavra_intermediaria

#     print(palavra_oculta)

#     if palavra_oculta == palavra_secreta:
#         print(f"Depois de {tentativas} você GANHOU!!!")
#         break



# FEITO PELO PROFESSOR
    
# palavra_secreta = 'perfume'
# letras_acertadas = ''
# numero_tentativas = 0

# while True:
#     letra_digitada = input('Digite uma letra: ')
#     numero_tentativas += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra.')
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'

#     print('Palavra formada:', palavra_formada)

#     if palavra_formada == palavra_secreta:
#         print('VOCÊ GANHOU!! PARABÉNS!')
#         print('A palavra era', palavra_secreta)
#         print('Tentativas:', numero_tentativas)
#         letras_acertadas = ''
#         numero_tentativas = 0