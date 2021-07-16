
class Nodo:
    def __init__(self ,dado ,ant ,prox):
        self.dado = dado
        self.ant = ant
        self.prox = prox

    def Nodo(self ,dado ,ant ,prox):
        self.dado = dado
        self.ant = ant
        self.prox = prox

    def __eq__(self ,other):
        return self.dado == other.dado

class linkedList:
    def __init__(self):
        self.tam = 0
        self.comeco = None
        self.fim = None

    def linkedList(self):
        self.tam = 0
        self.comeco = None
        self.fim = None

    # Esvazia a Lista Ligada, O(n)
    def clear(self):
        trav = self.comeco
        while trav is None:
            proximo = trav.prox
            trav.ant = trav.prox = None;
            trav.dado = None
            trav = proximo
        self.comeco = self.fim = trav = None
        self.tam= 0

    # Retorna Tanho
    def getTam(self):
        return self.tam

    def getCom(self):
        try:
            if self.ehVazia():
                raise IndexError('A Lista esta vazia')
            else:
                return self.comeco
        except IndexError as error:
            print(error)

    def getFim(self):
        try:
            if self.ehVazia():
                raise IndexError('A lista esta vazia')
            else:
                return self.comeco
        except IndexError as error:
            print(error)

    # ´Retorna se a lista se vazia
    def ehVazia(self):
        return self.getTam() == 0

    # Cria uma função de adicionar que tem como padrão adicionar ao fim da lista
    def add(self ,elem):
        self.addLast(elem)

    # Adiciona um elento ao inicio da Lista
    def addFirst(self ,elem):
        if self.ehVazia(): self.comeco = self.fim = Nodo(elem ,None ,None)
        else:
            self.comeco.ant = Nodo(elem ,None ,self.comeco)
            self.comeco = self.comeco.ant
        self.tam += 1

    # Adiciona um elemento ao final da fila
    def addLast(self, elem):
        if self.ehVazia():  self.fim = self.comeco = Nodo(elem, None ,None)
        else:
            self.fim.prox = Nodo(elem, self.fim ,None)
            self.fim = self.fim.prox
        self.tam += 1


    def removeFim(self):
        try:
            if self.ehVazia():
                raise IndexError('A lista é Vazia')
            else:
                data = self.fim.dado
                self.fim = self.fim.ant
                self.tam -= 1
            if self.ehVazia(): self.comeco = None
            else: self.fim.prox = None
            return data
        except IndexError as error:
            print(error)


    def removeComeco(self):
        try:
            if self.ehVazia():
                raise IndexError('A lista esta Vazia')
            else:
                data = self.comeco.dado
                self.comeco = self.comeco.prox
                self.tam -= 1
            if self.ehVazia(): self.fim = None
            else: self.comeco.ant = None
            return data
        except IndexError as erro:
            print(erro)


    def __remove(self ,nodo):
        if nodo.ant is None: return self.removeComeco()
        if nodo.prox is None: return self.removeFim()

        nodo.prox.ant = nodo.ant
        nodo.ant.prox = nodo.prox

        data = nodo.dado

        nodo.dado = None
        nodo = None

        self.tam -= 1

        return data

    def removeEm(self, index):
        try:
            if self.tam <= index < 0: raise IndexError('Out Of Boulds Exception')
            else:
                nodo = self.comeco
                if index < self.tam/2:
                    for i in range(index):
                        nodo = nodo.prox
                else:
                    for i in range(self.tam ,index ,-1):
                        nodo = nodo.prox

                self.__remove(nodo)
        except IndexError as error:
            print(error)

    def remove(self, value):
        nodo = self.comeco
        if value is None:
            while nodo is not None:
                if nodo.dado is None:
                    self.__remove(nodo)
                    return True
                nodo = nodo.prox
        else:
            while nodo is not None:
                if nodo.dado == value:
                    self.__remove(nodo)
                    return True
                nodo = nodo.prox
        return False

    def indexOf(self,value):
        index = 0
        nodo = self.comeco
        if value is None:
            while nodo is not None:
                if nodo.dado is None:
                    return index
                nodo = nodo.prox
                index+= 1
                if index > self.tam:
                    break
        else:
            while nodo is not None:
                if nodo.dado == value:
                    return index
                nodo = nodo.prox
                index += 1
                if index > self.tam:
                    break
        return -1

    def contains(self,value):
        return self.indexOf(value) != -1

    def toString(self):
        sb = "[ "
        nodo = self.comeco
        while nodo is not None:
            sb += str(nodo.dado)
            if nodo.prox is not None:
                sb += ','
            nodo = nodo.prox
        sb += ' ]'
        return sb