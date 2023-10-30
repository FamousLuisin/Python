import os

def listar(tarefas):
    if not tarefas:
        print('Nenhuma tarefa para ser listada')
        return
    
    print('===TAREFAS===')
    for tarefa in tarefas:
        print(tarefa)

def desfazer(tarefas, tarefas_desfeitas):
    try:
        tarefa_desfeitas = tarefas.pop()
        tarefas_desfeitas.append(tarefa_desfeitas)
    except IndexError:
        print('Não há nada em sua lista')

def refazer(tarefas, tarefas_desfeitas):
    if not tarefas_desfeitas:
        print('Nenhuma tarefa para ser refeita')
        return
    
    tarefa_refeita = tarefas_desfeitas.pop()
    tarefas.append(tarefa_refeita)

def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Não digitou nehuma tarefa')
        return
    tarefas.append(tarefa)


def main():
    tarefas = []
    tarefas_desfeitas = []

    while True:

        comandos = input('Digite uma tarefa ou comando [Listar, Desfazer, Refazer, clear, exit]: ')

        if comandos.upper() == 'LISTAR':
            listar(tarefas)

        elif comandos.upper() == 'DESFAZER':
            desfazer(tarefas, tarefas_desfeitas)
    
        elif comandos.upper() == 'REFAZER':
            refazer(tarefas, tarefas_desfeitas)

        elif comandos.upper() == 'CLEAR':
            os.system('cls')

        elif comandos.upper() == 'EXIT':
            break

        else:
            adicionar(comandos, tarefas)


main()
