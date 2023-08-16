a = float(input("Declare a quantidade de anos d idade:"))
m = float(input("Declare a quantidade de meses: "))
d = float(input("Declare a quantidade de dias: "))

anosDias = a *365
mesesDias = m * 30

diasTotais = anosDias + mesesDias + d
print(diasTotais)