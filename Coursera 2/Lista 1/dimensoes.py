def dimensoes(matriz):
  num_lin = len(matriz)
  
  if num_lin == 0:
    num_col = 0
  
  else:
    num_col = len(matriz[0])
  
  print(str(num_lin) + "X" + str(num_col))

