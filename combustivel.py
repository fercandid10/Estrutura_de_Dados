
tempo = float(input("Digite o tempo da viagem em horas: "))
vm = float(input("Informe a velocidade media: "))

distancia = tempo * vm

litros_usados = distancia / 12

print(f"Velocidade media: {vm}")
print(f"Tempo de viagem: {tempo}")
print(f"Distancia: {distancia}km")
print(f"Quantidade de litros {litros_usados}")
