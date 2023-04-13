#definir função fibo
def fibonacci(numero):
  #Conceitos base do fibonacci (recursivo)
  if numero < 2:
    return numero
  
  #chamar função de fibo -1, fibo -2
  else:
    return fibonacci(numero - 2) + fibonacci(numero - 1) 

def fibo(numero):
  #Conceitos base do fibonacci;
  if numero < 2:
    return numero
  
  #derivado de calculo de fibonacci;
  else:

    #iniciando variaveis;
    anterior = 0
    soma = 1

    #calcular fibonacci de numeros maior ou igual a 2;
    while numero >= 2:
      """o anterior é o anterior do anterior, enquanto a soma é o anterior, nesse caso,
      o anterior do anterior(anterior) ele recebe o anterior (soma) e o anterior(soma)
      rece a soma dele com o anterior do anterior (anterior)"""
      anterior, soma = soma, (soma + anterior)

      #diminui o numero
      numero -= 1
    
  return soma


