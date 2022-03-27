import numpy as np


class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade -1:
            return True
        else:
            return False

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A pilha esta cheia!')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print('A pilha esta vazia!')
        else:
            self.__topo -= 1

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1

pilha = Pilha(5)

for i in range(5):
    pilha.empilhar(i)

pilha.empilhar(6)
print(pilha.ver_topo())
print(pilha.desempilhar())
print('desempilhou 1')
print(pilha.desempilhar())
print('desempilhou 2')
print(pilha.desempilhar())
print('desempilhou 3')
print('pós desempilhar...')
print(pilha.ver_topo())
print('desempilhando novamente!')
print(pilha.desempilhar())
print(pilha.ver_topo())
print('por fim...')
print(pilha.desempilhar())
print(pilha.ver_topo())
print(pilha.desempilhar())

