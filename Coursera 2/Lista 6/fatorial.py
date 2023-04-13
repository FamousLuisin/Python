#def função fatorial
def fatorial(n):
  #conceitos basicos de fatorial, se ele for 0 ou 1 é igual a 1;
  if n <= 1:
    return 1
  
  else:
    #recursão, vai acabar criando uma sequência (chamada recursiva = Funão chamar a propria função)
    return n * fatorial(n-1)