
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostra_no(self):
        print(self.valor)

class ArvoreBinBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)
        #Se a arvore estiver vazia
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                # Esquerda
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        return
                #Direita
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo
                        return

    def pesquisar(self, valor):
        atual = self.raiz
        while atual.valor != valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if atual == None:
                return None
        return atual

    #Raiz, esquerda, direita
    def pre_ordem(self, no):
        if no != None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)
    #Esquerda, raiz, direita
    def em_ordem(self, no):
        if no != None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)
    #Esquerda, direita, raiz
    def pos_ordem(self, no):
        if no != None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)


    def excluir(self, valor):
        if self.raiz == None:
            print('A arvore esta vazia!')
            return

        #Encontrar o nó
        atual = self.raiz
        pai = self.raiz
        e_esquerda = True
        while atual.valor != valor:
            pai = atual
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            # Direita
            else:
                e_esquerda = False
                atual = atual.direita
            if atual == None:
                return False
        # O nó a ser apagado é uma folha
        if atual.esquerda == None and atual.direita == None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda == True:
                pai.esquerda = None
            else:
                pai.direita = None

        # O nó possui dois filhos
        else:
            sucessor = self.get_succesor(atual)

            if atual == self.raiz:
                self.raiz = sucessor
            elif e_esquerda == True:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor

            sucessor.esquerda = atual.esquerda
        return f'{valor} excluido!'


    def get_succesor(self, no):
        pai_sucessor = no
        sucessor = no
        atual = no.direita
        while atual != None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
        if sucessor != no.direita:
            pai_sucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita
        return sucessor
        

arvore = ArvoreBinBusca()

arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)

if arvore.pesquisar(100) == None:
    print('Elemento nao localizado')
else:
    print('Elemento localizado!')

print('-=' * 20)
arvore.pre_ordem(arvore.raiz)


tree = arvore.pesquisar(39)
print(tree)

print('-='*20)
ordem = arvore.em_ordem(arvore.raiz)
print(ordem)
print('-='*20)

pos_ordem = arvore.pos_ordem(arvore.raiz)
print(pos_ordem)
print('-=' * 20)
excluir = arvore.excluir(9)
print(excluir)
excluir = arvore.excluir(14)
print(excluir)
excluir = arvore.excluir(72)
print(excluir)

print('-=' * 20)
pos = arvore.pos_ordem(arvore.raiz)
print(pos)

