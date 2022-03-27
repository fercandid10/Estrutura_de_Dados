

lista = []

for i in range(5):
    num_int = int(input(f"Digite o {i+1}° valor: "))
    lista.append(num_int)
soma = 0
for c, a in enumerate(lista):
    soma += a

print(lista)
print(soma)






