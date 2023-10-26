# Modularização (separar o codigo em caixas / modulos)
# podemos organizar modulos em pacotes
# O primeiro modulo a ser executado se chama __main__
# Não é possivel importar arquivos ou pastas acima do arquivo main, só a baixo

import aula33_modulo # Só existe uma unica instancia

try:
    aula33_modulo.acessou()
    # aula33_modulo.acesso()
except AttributeError:
    print('Acesso negado, modulo invalido')