import numpy as np

class Deque:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade -1) or (self.inicio == self.final + 1)

    def __deque_vazio(self):
        return self.inicio == -1

    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print('O deque esta cheio')
            return

        # Se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        #Inicio estiver na primeira posicao
        elif self.inicio == 0:
            self.inicio = self.capacidade -1
        else:
            self.inicio -= 1

        self.valores[self.inicio] = valor

    def insere_final(self, valor):
        if self.__deque_cheio():
            print('O deque esta cheio!')
            return

        #Se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        #Final estiver na ultima posicao
        elif self.final == self.capacidade -1 :
            self.final = 0
        else:
            self.final += 1

        self.valores[self.final] = valor

    def excluir_inicio(self):
        if self.__deque_vazio():
            print('O deque ja esta vazio!')
            return

        #Possui somente um elemento
        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        else:
            #Volta para a posicao inicial
            if self.inicio == self.capacidade -1:
                self.inicio = 0
            else:
                #Incrementar inicio para remover o incio atual
                self.inicio += 1

    def excluir_final(self):
        if self.__deque_vazio():
            print('O deque ja esta vazio')
            return

        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        elif self.inicio == 0:
            self.final = self.capacidade -1
        else:
            self.final -= 1

    def get_inicio(self):
        if self.__deque_vazio():
            print('O deque esta vazio!')
            return
        return self.valores[self.inicio]

    def get_final(self):
        if self.__deque_vazio() or self.final < 0:
            print('O deque esta vazio!')
            return
        return self.valores[self.final]


deque = Deque(4)

#deque.insere_final(5)

#print(deque.get_inicio(), deque.get_final())
#deque.insere_final(10)
#print(deque.get_inicio(), deque.get_final())
deque.insere_inicio(10)
#print(deque.get_inicio(), deque.get_final())
deque.insere_inicio(20)
deque.insere_final(30)
deque.insere_final(40)
#print(deque.get_inicio(), deque.get_final())
deque.excluir_inicio()
deque.excluir_final()
print(deque.get_inicio(), deque.get_final())
print(deque.valores)
