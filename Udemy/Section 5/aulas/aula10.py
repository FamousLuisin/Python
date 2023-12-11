# Relação entre classes: associação, agregação e composição;
# Associação é um tipo de relação entre objetos (Estão ligados dentro de um sistema);
# É a relação mais comum entre objetos e tem subconjuntos (agregação e composição);
# Geralmente associação é quando um objeto tem um atributo que referencia outro objeto;

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Ferramenta:
    def __init__(self,nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} esta escrevendo'

# Associação    
escrito = Escritor("Noki")
pincel = Ferramenta("Pincel")
maquina = Ferramenta("maquina")

escrito.ferramenta = maquina

print(pincel.escrever())
print(maquina.escrever())
print(escrito.ferramenta.escrever())
