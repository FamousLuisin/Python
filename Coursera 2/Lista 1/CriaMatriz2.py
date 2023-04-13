def criaMatriz(linhas, colunas):
  matriz = []
  for i in range(linhas):
    linha = []
    for j in range(colunas):
      valor = float(input("Digite o elemneto [{}][{}]: ".format(i+1, j+1)))
      linha.append(valor)
    matriz.append(linha)
  return matriz

def le_matriz():
  linhas = int(input("numero de linhas: "))
  colunas = int(input("numero de colunas: "))
  
  matriz = criaMatriz(linhas, colunas)

  ordenaMatriz(matriz)
  

def ordenaMatriz(matriz):
  for linha in matriz:
    print(linha)

le_matriz()
