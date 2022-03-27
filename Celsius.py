def celcius_fahrenheit():
    celcius = int(input("Informe a temperatura C°: "))
    f = (9 * celcius + 160) / 5
    return f

def celcius_fahrenheit2(c=int(input("Informe a temperatura C°: "))):
    f = (9 * c + 160) / 5
    return f

print(celcius_fahrenheit())
print(celcius_fahrenheit2())

