# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

import os

caminho_pasta = 'C:\\Users\\lufim\\Documents\\GitHub\\Python\\Udemy\\Section 4\\aulas\\aula47\\'
caminho_arquivo = caminho_pasta + 'aula47.txt'

# open abre o arquivo
# arquivo = open(caminho_arquivo, 'w')
# # close fecha o arquivo
# arquivo.close()

# with ele abre e fecha o arquivo sempre
# w+ e r+, podem tanto ler quanto escrever no arquivo
# w apaga tudo e recria o arquivo
with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    # write: Escrever algo no arquivo
    arquivo.write('atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    # writelines: manda um iteravel para adicionar no arquivo
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0) # Mover o cursor para o topo (caso não faça isso nem tem como ler ele)
    print(arquivo.read())

print('#' * 10, '\n')

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    # read: Ler algo do arquivo
    print(arquivo.read())

print('#' * 10, '\n')

with open(caminho_arquivo, 'r+', encoding='utf-8') as arquivo:
    print('READLINES\n')
    # end='' and .strip(): Remover quebra de linha desnecessaria
    for linha in arquivo.readlines():
        print(linha.strip())

print('#' * 10, '\n')

# a adiciona novas linhas sem apagar nada
with open(caminho_arquivo, 'a+') as arquivo:
    # write: Escrever algo no arquivo
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    # writelines: manda um iteravel para adicionar no arquivo
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# Remover um arquivo, ele e o remove
# os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo)

# renomear arquivo
# os.rename(caminho_arquivo, caminho_pasta + 'aula47-2.txt')
