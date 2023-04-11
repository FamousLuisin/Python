"""

====================================================================================
String são objetos imutaveis
a = "banana"
b = "banana"
c = "maçã"

Como string são imutaveis, a e b estão apontando para o mesmo espaço de memoria,
que esta guardando o objeto/string "banana".
Então:  a is b > True (Ambas referencias apontam para o mesmo objeto);
        a is c > False (Ambas referencias apontam para objetos diferentes);

No caso de a e c, eles não estao apontando para o mesmo objeto.
====================================================================================
Listas são mutaveis

a = [1, 2, 3]
b = [1, 2, 3]

Como listas são mutaveis, a e b apontam para objetos diferente, mesmo que o conteudo
dentro dele seja igual.
Então:  a is b > False (Ambas referencias apontam para objetos diferentes)
        a == b > True (O conteudo dentro de a e b é o mesmo)
====================================================================================
Lista = [1, 2 , 3]
Lista * 3 > [1, 2 , 3, 1, 2 , 3, 1, 2 , 3]
[Lista] * 3 > [[1, 2 , 3], [1, 2 , 3], [1, 2 , 3]]



"""