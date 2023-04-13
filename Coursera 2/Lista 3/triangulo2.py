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
    self.p = self.a + self.b + self.c

    #retonar o valor de perimetro;
    return self.p

  #Criar metdo para o tipo de triangulo;
  def tipo_lado(self):
   
    #Verificar se ele é escaleno(Nenhum lado igual);
    if self.a != self.b and self.a != self.c and self.b != self.c:
      self.tipo = "escaleno"
    
    else:
      #Verificar se é equilátero(Todos os lados iguais);
      if self.a == self.b and self.a == self.c and self.b == self.c:
        self.tipo = "equilátero"
      
      #Se ele não for nenhum dos anteriores será isósceles(Dois lados iguais);
      else:
        self.tipo = "isósceles"
    
    return self.tipo

