# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
# Todas as operações com objetos se usa um dunder método

class Cordenada():
    # Métod init
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y

    # Método str = O retorno qualquer do objeto
    def __str__(self):
        return f'({self.x}, {self.y})'

    # Método repr = Representação do objeto (Para desenvolvedor)
    # Mostrar como aquele objeto é montado
    def __repr__(self):
        # Pegar o nome da classe
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        # Quando usamos o repr devemos usar o !r como boa pratica
        # Para o outro desenvolvedor saber exatamente oq eé o metodo
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

p1 = Cordenada(1, 2)
p2 = Cordenada(5, 5)

print(p1)
# Retornar um repr, caso tenha uma str
print(repr(p2))
print(f'{p2!r}')

