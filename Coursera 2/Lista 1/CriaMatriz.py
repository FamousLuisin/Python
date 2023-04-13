def criaMatriz(linhas, colunas, valor):
  matriz = []
  for i in range(linhas):
    linha = []
    for j in range(colunas):
      linha.append(valor)
    matriz.append(linha)
  return matriz



def imprime_matriz(matriz):
  for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
      if coluna < len(matriz[linha]) - 1:
        print(matriz[linha][coluna], end=' ')
      
      else:
        print(matriz[linha][coluna])


"""def imprime_matriz(matriz):
  for linha in matriz:
    for coluna in linha:
      print(coluna, end=' ')"""