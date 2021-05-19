class ListaNaoOrdenada:
    def __init__(self):
        self.inicio = None

    def vazia(self):
        return self.inicio == None

    def inserir(self, valor):
        temp = No(valor)
        temp.setarProximo(self.inicio)
        self.inicio = temp

    def buscar(self, item):
        atual =  self.inicio
        encontrou = False
        while atual != None and not encontrou:
            if atual.obterValor() == item:
                encontrou = True
            else:
                atual = atual.obterProximo()
        
        return encontrou

    def tamanho(self):
        atual =  self.inicio
        contador = 0
        while atual != None:
           contador = contador + 1
           atual = atual.obterProximo()

        return contador
    
    def imprimir(self):
        atual =  self.inicio
        while atual != None:
            print(atual.obterValor())
            atual = atual.obterProximo()

    def remover(self, i):
        if self.inicio == None:
            return 'Lista vazia!'
        elif self.inicio == i:
            self.inicio = self.inicio.obter
            proximo()
        else:
            antes = self.inicio.proximo
            atual = antes.obterproximo()
            while atual != None:
                if atual == i:
                    antes.setarproximo(atual.obterproximo())
                    i.setproximo(None)
                    return True
                antes = atual
                atual = atual.obterproximo()




lista = ListaNaoOrdenada()


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def obterValor(self):
        return self.valor
    
    def setarValor(self, valor):
        self.valor = valor
    
    def obterProximo(self):
        return self.proximo
    
    def setarProximo(self, prox):
        self.proximo = prox

    def __str__(self):
        return f'[{self.obterValor()}]'


class Fila:
    def __init__(self):
        self.items = []

    def inverter(self):
        pilha = Pilha()

        while self.tamanho() > 0:
            item = self.desenfileirar()
            pilha.empilhar(item)

        while pilha.tamanho() > 0:
            item = pilha.desempilhar()
            self.enfileirar(item)

    def imprimir(self):
        return "🚶🏻⬅️  ".join(self.items)

    def vazia(self):
        return self.items == []

    def tamanho(self):
        return len(self.items)

    def enfileirar(self, item): # inserir
        self.items.append(item)

    def desenfileirar(self): # remover
        return self.items.pop(0)

    def frente(self):
        return self.items[0]


class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, valor):
        self.items.append(valor)

    def desempilhar(self):
        return self.items.pop()

    def tamanho(self):
        return len(self.items)

    def vazia(self):
        return self.items == []
