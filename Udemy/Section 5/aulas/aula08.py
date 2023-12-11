# @property - Um getter e setter no modo pythonico
# getter - um método para obter um atributo
# setter - um metodo para
# cor -> get_cor (Obter valor)
# @property - Método, mas se comporta como atributo
# Geralmente é usada como:
# - Como getter
# - evitar a quebra de código cliente (codigo que usa seu codigo)
# - habilitar setter
# - executar ação ao obter um atributo

class Caneta:
    
    def __init__(self, cor):
        # Não use esse atributo fora da classe (já quele ele começa com _)
        # Mesmo que dizer que aquele codigo é private / protected
        self._cor = cor

    # getter
    @property
    def cor(self):
        return self._cor
    
    # setter
    @cor.setter
    def cor(self, valor):
        self._cor = valor



caneta = Caneta('Azul')
print(caneta.cor)
# Quando usa o = nesse caso ele mandará o valor senguinte como atributo do setter
caneta.cor = 'Vermelho'

print(caneta.cor)
# print(caneta.cor_tampa)