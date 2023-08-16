distancia = float(input("digite a distancia percorrida: "))
gasolina = float(input("digite a quantidade de gasolina: "))

consumo = distancia/gasolina

if consumo < 8:
    print("Venda o carro")
elif consumo <= 8 and  consumo >= 8:
    print("Economico")
elif consumo > 12:
    print("Super Economico")