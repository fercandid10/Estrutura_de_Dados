import numpy as np

class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []


    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)


    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)


class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo


class Grafo:
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)

    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))

    zerind.adiciona_adjacente(Adjacente(arad, 75))
    zerind.adiciona_adjacente(Adjacente(oradea, 71))

    oradea.adiciona_adjacente(Adjacente(zerind, 71))
    oradea.adiciona_adjacente(Adjacente(sibiu, 151))

    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(arad, 140))
    sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

    dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
    dobreta.adiciona_adjacente(Adjacente(craiova, 120))

    craiova.adiciona_adjacente(Adjacente(dobreta, 120))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))
    craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

    rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
    rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

    fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

    pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

    bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
    bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
    bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))





class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1

        self.__valores = np.empty(self.__capacidade, dtype=object)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
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
        #Retorna o elemento desempilhado
        if self.__pilha_vazia():
            print('A pilha esta vazia!')
            return None
        else:
            tmp = self.__valores[self.__topo]
            self.__topo -= 1
            return tmp

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1

class BuscaProfundidade:
    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.visitado = True
        self.pilha = Pilha(20)
        self.pilha.empilhar(inicio)

    def buscar(self):
        topo = self.pilha.ver_topo()
        print(f'Topo: {topo.rotulo}')
        for adjacente in topo.adjacentes:
            print(f'Topo é {topo.rotulo}. {adjacente.vertice.rotulo} ja foi visitada? {adjacente.vertice.visitado}')
            if adjacente.vertice.visitado == False:
                adjacente.vertice.visitado = True
                self.pilha.empilhar(adjacente.vertice)
                print(f'Empilhou {adjacente.vertice.rotulo}')
                self.buscar()
        print(f'Desempilhou {self.pilha.desempilhar().rotulo}')
        print()


class FilaCircular:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0

        #Mudança no tipo de dado
        self.valores = np.empty(self.capacidade, dtype=object)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila esta cheia!')
            return

        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila ja esta vazia!')
            return

        tmp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        self.numero_elementos -= 1
        return tmp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]


class BuscaLargura:

    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.visitado = True
        self.fila = FilaCircular(20)
        self.fila.enfileirar(inicio)

    def buscar(self):
        primeiro = self.fila.primeiro()
        print('-=' * 20)
        print(f'Primeiro da fila: {primeiro.rotulo}')
        tmp = self.fila.desenfileirar()
        print(f'Desenfileirou: {tmp.rotulo}')
        for adjacente in primeiro.adjacentes:
            print(f'Primeiro elemento era {tmp.rotulo}. {adjacente.vertice.rotulo} ja foi visitado? {adjacente.vertice.visitado}')
            if adjacente.vertice.visitado == False:
                adjacente.vertice.visitado = True
                self.fila.enfileirar(adjacente.vertice)
                print(f'Enfileirou: {adjacente.vertice.rotulo}')
        if self.fila.numero_elementos > 0:
            self.buscar()


class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        #Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)

    #Referencia para o vertice e comparação com a distancia para o objetivo
    # Referencia para o vertice e comparação com a distancia A*
    #def insere(self, vertice):
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade maxima atingida!')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            #if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:

                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        #self.valores[posicao] = vertice
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor esta vazio!')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'{i} - {self.valores[i].vertice.rotulo} - {self.valores[i].custo} - {self.valores[i].vertice.distancia_objetivo} - {self.valores[i].distancia_aestrela}')

class Gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('-=' * 20)
        print(f'Atual: {atual.rotulo}')
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente.vertice)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0])

class AEstrela:

    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('-=' * 20)
        print(f'Atual: {atual.rotulo}')
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].vertice)



grafo = Grafo()
'''
print(grafo.arad.mostra_adjacentes())
print('-=' * 20)
print(grafo.bucharest.mostra_adjacentes())
print('-=' * 20)
pilha = Pilha(5)
pilha.empilhar(grafo.arad)
pilha.empilhar(grafo.sibiu)
pilha.empilhar(grafo.timisoara)
print(pilha.ver_topo().rotulo)
print('-=' * 20)
print(pilha.desempilhar().rotulo)
print('-=' * 20)
print(pilha.desempilhar().rotulo)
print('-=' * 20)
print(pilha.ver_topo().rotulo)
print('-=' * 20)
'''
'''
buscaProfundidade = BuscaProfundidade(grafo.arad)
buscaProfundidade.buscar()
print('-=' * 20)
print(buscaProfundidade.pilha.ver_topo())
print('-=' * 20)
'''

'''
fila = FilaCircular(20)
fila.enfileirar(grafo.arad)
fila.enfileirar(grafo.bucharest)
fila.enfileirar(grafo.fagaras)

print(fila.primeiro().rotulo)
print('-=' * 20)
print(fila.desenfileirar().rotulo)
print('-=' * 20)
print(fila.primeiro().rotulo)
print('-=' * 20)
buscaLargura = BuscaLargura(grafo.arad)
buscaLargura.buscar()
print('-=' * 20)
print(buscaLargura.fila.numero_elementos)
'''
'''
vetor = VetorOrdenado(5)
vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)
vetor.insere(grafo.lugoj)
vetor.imprime()
print(vetor.valores[0], vetor.valores[0].rotulo)
print('-=' * 20)

busca_gulosa = Gulosa(grafo.bucharest)
busca_gulosa.buscar(grafo.arad)
'''

print(grafo.arad.adjacentes[0].vertice.rotulo, grafo.arad.adjacentes[0].vertice.distancia_objetivo)

print(grafo.arad.adjacentes[0].distancia_aestrela, grafo.arad.adjacentes[0].custo)

vetor = VetorOrdenado(3)
vetor.insere(grafo.arad.adjacentes[0])
vetor.insere(grafo.arad.adjacentes[1])
vetor.insere(grafo.arad.adjacentes[2])

vetor.imprime()
print('-=' * 20)
busca_aestrela = AEstrela(grafo.bucharest)
busca_aestrela.buscar(grafo.arad)

