from dataclasses import dataclass, field

@dataclass()
class Pessoa:
    nome: str = field(default='Missing')
    # repr = False retira aquele parametro do repr
    sobrenome: str = field(default='Not sent', repr=False)
    idade: int = 0 # Podemos fornecer tbm valores padroes (Pórem so os imutaveis)
    enderecos:list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa()
    print(p1)