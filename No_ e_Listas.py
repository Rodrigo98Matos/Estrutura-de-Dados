class No:                                           #Cria referencias entre variáveis
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def setvalor(self, novo_valor):                 #atribui um novo valor
        self.valor = novo_valor

    def setproximo(self, proximo):                  #Atribui novo valor ao proximo
        self.proximo = proximo

    def getvalor(self):                             #retorna o valor solicitado, presente na lista
        return self.valor

    def getproximo(self):                           #Retorna o proximo valor da lista
        return self.proximo
    
class ListaNaoOrdenada:                             #estrutura para lista encadeada
    def __init__(self):
        self.inicio = None

    def vazia(self):                                #verifica se a lista está vazia
        return self.inicio == None

    def inserir(self, item):                        #adiciona valores à lista
        temp = No(item)                             #inicia a função nó
        temp.setproximo(self.inicio)                #gera um vinculo com o valor de inicio da lista
        self.inicio = temp                          #O novo item assume o inicio da lista

    def buscar(self, item):                         #confirma se o valor está presente na lista
        atual = self.inicio
        encontrou = False
        while atual != None and not encontrou:
            if atual.getvalor() == item:
                encontrou = True
            else:
                atual = atual.getproximo()
        return encontrou

    def tamanho(self):                              #quantidade de valores da lista
        atual = self.inicio
        contador = 0
        while atual != None:
            contador += 1
            atual = atual.getproximo()
        return contador

    def imprimir(self):                             #Imprime os valores da lista
        at = self.inicio
        while at != None:
            print(at.getvalor())
            at = at.getproximo()
        if self.vazia():
            return 'Lista vazia!'
        
    def remover(self, i):
        if self.buscar(i):                          #testa se o item está na lista
            if i == self.inicio.getvalor():         #para remover o valor de inicio da lista
                at = self.inicio.getproximo()
                self.inicio = at
                if not self.vazia():                #evita erro, quando se está removendo um item de uma lista com apenas um item
                    self.proximo = at.getproximo()
                
            else:                                   #para remover item do meio da lista
                ant = self.inicio                   #conserva o valor do item anterior
                at = self.inicio.proximo
                while at:                           #O laço é mantido enquanto tem valores a serem analisados na lista
                    if i == at.getvalor():          #para quando encontrar o item a ser removido
                        ant.proximo = at.proximo    #cria uma referencia do item anterior ao item posterior do item a ser removido da lista
                        break                       #interempe o laço
                    ant = at                        #conserva o item anterior
                    at = at.getproximo()            #avança para o proximo item da lista
            return f"^_^ O item '{i}' foi removido com sucesso! ^_^"    
        
        else:                                       #caso o item não estaja na lista
            return f"¯\_(ツ)_/¯ O item '{i}' não está na lista! ¯\_(ツ)_/¯"

lista = ListaNaoOrdenada()                          #Simplifica o acesso a função

periodo1 = ListaNaoOrdenada()
periodo2 = ListaNaoOrdenada()
periodo3 = ListaNaoOrdenada()
periodo4 = ListaNaoOrdenada()
periodo5 = ListaNaoOrdenada()
periodo6 = ListaNaoOrdenada()
