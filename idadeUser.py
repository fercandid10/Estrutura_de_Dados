def idade(a = int(input("Informe sua idade: "))):
    if (a >=0 and a <=12):
        print("Criança!")
    elif (a >=13 and a<=17):
        print("Adolescente!")
    elif (a >=18):
        print("Adulto!")
    else:
        print(f"{a} idade invalida!")


idade()

