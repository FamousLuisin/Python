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



