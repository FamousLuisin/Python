"""
class carro: #Criar classe vazia
  pass

carroMeu = carro() #Instancia dentro do objeto carro;
carroSeu = carro() #Instancia dentro do objeto carro;

carroMeu.ano = 2000 #Recebe um novo atributo referente ao ano
carroMeu.modelo = 'Ford' #Recebe um novo atributo referente ao modelo
carroMeu.cor = 'Preto' #Recebe um novo atributo referente a cor


class carro: #Criar classe vazia
  def __init__(self, modelo, ano, cor):
    self.modelo = modelo
    self.ano = ano

self é o proprio objeto a ser criado;

"""