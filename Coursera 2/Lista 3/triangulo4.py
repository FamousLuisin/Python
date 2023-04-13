#Criar classe de triangulo;
class Triangulo:
  
  #Criar metodo de construção;
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  #Criar metodo para calcular perimetro;
  def perimetro(self):
  
    #valor do atributo perimetro;
    perimetro = self.a + self.b + self.c

    #retonar o valor de perimetro;
    return perimetro

  #Criar metodo para o tipo de triangulo;
  def tipo_lado(self):
   
    #Verificar se ele é escaleno(Nenhum lado igual);
    if self.a != self.b and self.a != self.c and self.b != self.c:
      return  print("escaleno")
    
    else:
      #Verificar se é equilátero(Todos os lados iguais);
      if self.a == self.b and self.a == self.c and self.b == self.c:
        return  print("equilátero")
      
      #Se ele não for nenhum dos anteriores será isósceles(Dois lados iguais);
      else:
        return  print("isósceles")
  
  #Criar metodo para triangulo retangulo;
  def retangulo(self):
    #verificar se o tringulo é retangulo ou não;
    if ((self.a**2) + (self.b**2)) == (self.c**2):
      return True
    
    #Se passar pelo if ele não é retangulo;
    else:
      return False
  
  #Criar metodo de semelhança entre triangulo
  def semelhantes(self, triangulo):

    #Verificar se são semelhantes(Serão semelhantes se a razão (divisão) entre os comprimentos dos seus lados forem iguais.)
    if (self.a / triangulo.a == self.b / triangulo.b) and (self.a / triangulo.a == self.c / triangulo.c):
      return True
    
    else: 
      return False
