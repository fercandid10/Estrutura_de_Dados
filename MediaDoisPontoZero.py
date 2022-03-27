def calculo():
    aux = 0
    for i in range(5):
        a = float(input(f"Informe a {i+1}° nota:"))
        aux += a
    media = aux / 5
    print(f"A media foi de {media}")

calculo()
