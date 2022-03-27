import numpy as np
import sys

vertices = {'arad': 0, 'zerind': 1, 'oradea': 2, 'sibiu': 3, 'timisoara': 4,
            'lugoj': 5, 'mehadia': 6, 'dobreta': 7, 'craiova': 8, 'rimnicu': 9,
            'fagaras': 10, 'pitesti': 11, 'bucharest': 12, 'giurgiu': 13}

cidades = {0: 'arad', 1: 'zerind', 2: 'oradea', 3: 'sibiu', 4: 'timisoara', 5: 'lugoj',
           6: 'mehadia', 7: 'dobreta', 8: 'craiova', 9: 'rimnicu', 10: 'fagaras', 11: 'pitesti',
           12: 'bucharest', 13: 'giurgiu'}

arestas = np.zeros([len(cidades), len(cidades)], dtype=int)

print(arestas.shape)

arestas[vertices['arad'], [vertices['zerind']]] = 75
arestas[vertices['arad'], [vertices['sibiu']]] = 140
arestas[vertices['arad'], [vertices['timisoara']]] = 118

arestas[vertices['zerind'], [vertices['arad']]] = 75
arestas[vertices['zerind'], [vertices['oradea']]] = 71

arestas[vertices['oradea'], [vertices['zerind']]] = 71
arestas[vertices['oradea'], [vertices['sibiu']]] = 151

arestas[vertices['sibiu'], [vertices['oradea']]] = 151
arestas[vertices['sibiu'], [vertices['arad']]] = 140
arestas[vertices['sibiu'], [vertices['fagaras']]] = 99
arestas[vertices['sibiu'], [vertices['rimnicu']]] = 80

arestas[vertices['timisoara'], [vertices['arad']]] = 118
arestas[vertices['timisoara'], [vertices['lugoj']]] = 111

arestas[vertices['lugoj'], [vertices['timisoara']]] = 111
arestas[vertices['lugoj'], [vertices['mehadia']]] = 70

arestas[vertices['mehadia'], [vertices['lugoj']]] = 70
arestas[vertices['mehadia'], [vertices['dobreta']]] = 75

arestas[vertices['dobreta'], [vertices['mehadia']]] = 75
arestas[vertices['dobreta'], [vertices['craiova']]] = 120

arestas[vertices['craiova'], [vertices['dobreta']]] = 120
arestas[vertices['craiova'], [vertices['pitesti']]] = 138
arestas[vertices['craiova'], [vertices['rimnicu']]] = 146

arestas[vertices['rimnicu'], [vertices['craiova']]] = 146
arestas[vertices['rimnicu'], [vertices['sibiu']]] = 80
arestas[vertices['rimnicu'], [vertices['pitesti']]] = 97

arestas[vertices['fagaras'], [vertices['sibiu']]] = 99
arestas[vertices['fagaras'], [vertices['bucharest']]] = 211

arestas[vertices['pitesti'], [vertices['rimnicu']]] = 97
arestas[vertices['pitesti'], [vertices['craiova']]] = 138
arestas[vertices['pitesti'], [vertices['bucharest']]] = 101

arestas[vertices['bucharest'], [vertices['fagaras']]] = 211
arestas[vertices['bucharest'], [vertices['pitesti']]] = 101
arestas[vertices['bucharest'], [vertices['giurgiu']]] = 90

print('-=' * 20)
print(arestas)
print('-=' * 20)

class Dijkstra:
    def __init__(self, vertices, arestas, inicio):
        self.tamanho = len(vertices)
        self.vertices = vertices
        self.grafo = arestas
        self.inicio = inicio

    def mostra_solucao(self, distancias):
        print(f'Menores distancias de {self.vertices[self.inicio]} ate todos os outros.')
        for vertice in range(self.tamanho):
            print(self.vertices[vertice], distancias[vertice])

    def distancia_minima(self, distancia, visitados):
        minimo = sys.maxsize
        for vertice in range(self.tamanho):
            if distancia[vertice] < minimo and visitados[vertice] == False:
                minimo = distancia[vertice]
                indice_minimo = vertice
        return indice_minimo

    def dijkstra(self):
        distancia = [sys.maxsize] * self.tamanho
        distancia[self.inicio] = 0
        visitados = [False] * self.tamanho

        for _ in range(self.tamanho):
            indice_minimo = self.distancia_minima(distancia, visitados)
            visitados[indice_minimo] = True
            for vertice in range(self.tamanho):
                if self.grafo[indice_minimo][vertice] > 0 and visitados[vertice] == False and distancia[vertice] > distancia[indice_minimo] + self.grafo[indice_minimo][vertice]:
                    distancia[vertice] = distancia[indice_minimo] + self.grafo[indice_minimo][vertice]

        self.mostra_solucao(distancia)


dijkstra = Dijkstra(cidades, arestas, vertices['arad'])
print(dijkstra.dijkstra())

