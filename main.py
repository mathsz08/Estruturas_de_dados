from LkdLst import Linked_List as LL

def linha():
    print('-'*70)

def lista_ligada():
    lista = LL.linkedList()
    linha()
    print('Lista Ligada Funções: Adicionar, Remover, Vizualizar e Procurar')
    linha()
    while True:
        print('Adicione elementos')
        v = input("Escreva qualquer valor ou 'S' para sair: ")
        if v != 'S':
            lista.add(v)
        else:
            break
    linha()
    while True:
        print(f'Remova valores de sua lista: {lista.toString()}')
        v = input("Escreva um valor para remover de sua lista ou 'S' para sair: ")
        if v != 'S':
            print(lista.remove(v))
        else:
            break

    while True:
        linha()
        print(f'Procure valores em sua Lista Ligada')
        v = input("Escreva um valor para procurar em sua lista: ")
        linha()
        if v != 'S':
            if lista.contains(v):print('Sim, esta em sua lista')
            else:print('Não, não esta em sua lista')
        else:
            break


def pilha():
    pass


def fila():
    pass


def fila_de_Prioridades():
    pass


estruturas = {1: ('Lista Duplamente Ligada', 'lista_ligada'),
              2: ('Pilha', 'pilha'),
              3: ('Fila', 'fila()'),
              4: ('Fila de Prioridades', 'fila_de_Prioridades')}

while True:
    linha()
    print("Ola, Escolha uma estrutura de dados:")
    for n, i in enumerate(estruturas.values()):
        print(f"{n + 1} - {i[0]}")
    print("0 - Para sair do sistema")
    r = int(input('Digite um numero: '))
    if r != 0:
        print(locals()[estruturas.get(r)[1]]())
    else:
        break
