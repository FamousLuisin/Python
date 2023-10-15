import os

lista_de_compras = []

while True:
    escolha = input("Deseja [A]dicionar, [E]xcluir, [L]istar, [S]air: ").upper()

    if escolha == "A":
        os.system("cls")
        novo_item = input("Adicionar novo item: ")
        lista_de_compras.append(novo_item)
    elif escolha == "E":
        os.system("cls")
        excluir_item = input("Qual item [index] deseja excluir? ")

        try:
            excluir_item = int(excluir_item)
            lista_de_compras.pop(excluir_item)
            # del lista_de_compras[excluir_item]
        except ValueError:
            print("Isso não é um numero!")
        except IndexError:
            print("Está fora do index")
        
    elif escolha == "L":
        os.system("cls")
        if lista_de_compras:
            for indice, item in enumerate(lista_de_compras):
                print(f"{indice + 1}: {item}")
        else:
            print("Não há nada na lista")
    elif escolha == "S":
        os.system("cls")
        print("Fim")
        break
    else:
        os.system("cls")
        print("Erro")
        continue