class Fila():
    def __init__(self):
        self.itens = list()
    def enfileirar(self, item):
        self.itens.append(item)
    def desenfileirar(self):
        return self.itens.pop(0)
    def tamanho(self):
        return len(self.itens)
    def vazia(self):
        return self.itens == []
    def frente(self):
        return self.itens[0]
f = Fila()
