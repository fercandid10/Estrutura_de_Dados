import numpy as np

def bubleSort(vetor):
    n = len(vetor)

    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp

    return vetor

buble = bubleSort(np.array([15, 34, 8, 3]))

print(buble)

