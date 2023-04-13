def soma_matrizes(m1, m2):
  num_lin1 = len(m1)
  num_col1 = len(m1[0])
  
  num_lin2 = len(m2)
  num_col2 = len(m2[0])

  if num_lin1 == num_lin2 and num_col1 == num_col2:
    new_matriz = []
    for i in range(num_lin1):
      linha = []
      for j in range(num_col1):
        linha.append(m1[i][j] + m2[i][j])
      new_matriz.append(linha)
    return new_matriz
  
  else:
    return False

print(soma_matrizes([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 20, 30], [40, 50, 60],[70, 80, 90]]))