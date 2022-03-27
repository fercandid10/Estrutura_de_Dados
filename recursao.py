#Sem recursao
import math

def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

somando = soma1(5)
print('Sem recursao', somando)

#Com recursao
def soma2(n):
    if n == 0:
        return 0

    return n + soma2(n - 1)

somaRecursao = soma2(5)
print('Com recursao', somaRecursao)




num = int(input("Digite um numero: "))

