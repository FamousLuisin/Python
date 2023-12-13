class Cordenada():
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'
    
    # Retornar o que vc quiser na hora de fazer uma adição entre duas classes
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Cordenada(novo_x, novo_y)
    
    # Retornar o que vc quiser na hora de fazer uma compração de menor e maior
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other

if __name__ == '__main__':
    p1 = Cordenada(1, 2)
    p2 = Cordenada(5, 5)
    p3 = p1 + p2
    print(p3)
    print('p1 é maior que p2:', p1 > p2)
    print('p2 é maior que p1:', p2 > p1)