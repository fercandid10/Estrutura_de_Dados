def calculo(a = float(input("Informe n1:")), b= float(input("Informe a n2:")), c= float(input("Informe a n3: "))):
    media = (a + b + c)/ 3
    if (media > 6):
        print(f"Parabéns {media}, aprovado!")
    elif (media <=4):
        print(f"{media} Reprovado!")
    elif (media >4 and media<=6):
        print(f"{media} Exame!")


calculo()

