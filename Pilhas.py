class Pilha():
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if len(self.itens) != 0:
            return self.itens.pop()
        else:
            print('Pilha vazia')

    def vazia(self):
        return self.itens == []

    def topo(self):
        if len(self.itens) != 0:
            return self.itens[-1]
        else:
            return 'Pilha vazia'
    def tamanho(self):
        return len(self.itens)

    
p = Pilha()
