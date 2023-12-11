# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        # Criar o endereço (conexao com outra classe) dentro da classe pai
        # Quando a classe pai for deletada, todos os filhos tbm iram ser
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar(self):
        for endereco in self.enderecos:
            print(f'{endereco.rua}: {endereco.numero}')

    def __del__(self):
        print('Apagando:', self.nome)


class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Apagando:', self.rua, self.rua)


cliente = Cliente("Jemmys")
cliente.inserir_endereco('Av Brasil', 89)
cliente.inserir_endereco('Brasília', 785)
endereco_externo = Endereco('Av Saudade', 55)
cliente.inserir_endereco_externo(endereco_externo)
cliente.listar()

# Ao apagar o cliente, todos os endereços vao juntos (Composição)
del cliente

print('FIM')