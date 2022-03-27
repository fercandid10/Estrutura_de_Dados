#Notaçao Big-O
'''
 Como comparar dois algoritmos?
 Comparaçao objetiva entre algoritmos
 Considera diferenças entre poder de processamento, sistema operacional, linguagem de programacao
 O quanto a "complexidade" do algoritmo aumenta de acordo com as entradas
'''

'''
#Ex01
#11 passos ou n, depende do parametro.. O(n)
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma
print(soma1(10))

#3 passos O(3)
def soma2(n):
    return (n * (n + 1)) / 2
print(soma2(10))
'''
'''
#Ex02
def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista
print(lista1())

def lista2():
    return range(1000)
l = lista2()

for i in l:
    print(i)
'''
from math import log
import numpy as np
import matplotlib.pyplot as plt
'''
n = np.linspace(1,10,100)
labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape), np.log(n), n, n* np.log(n), n**2, n**3, 2**n]

print(plt.figure(figsize=(10,8)))
print(plt.ylim(0,100))
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')
plt.show()

'''
#CONSTANT - 0(1) UM UNICO PASSO
lista = [1,2,3,4,5]
def constant(n):
    print(n[0])

#constant(lista)

#Linear - O(n)
def linear(n):
    for i in n:
        print(i)

#linear(lista)

#Quadratic - O(n^2)
def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)

#quadratic(lista)

#Combination
def combination(n):
    print(n[0])  #o(1)

    for i in range(5): #o(5)
        print('test', i)

    for i in n: #o(n)
        print(i)

    for i in n: # o(n)
        print(i)

    #O(3)
    print('Python')
    print('Python')
    print('Python')
# total O(9) + O(n)
combination(lista)

