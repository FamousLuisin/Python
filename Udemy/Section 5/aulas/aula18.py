# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name
    
    @property
    @abstractmethod
    def name(self): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inutil')

    @property
    def name(self):
        return self._name

    # Caso tenha feito o getter em uma classe pai e queria usar o setter no filho
    # @ClassePai.NameProperty.setter
    @name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)