salario = float(input("Digite seu salario: "))

aliquota = 0
deducao = 0

if salario <= 1903.99:
    aliquota = 0
    deducao = 0

elif salario > 1903.99 &  salario <= 2826.65:
    aliquota = 0.075
    deducao = 142.80

elif salario > 2826.66 & salario <= 3751.05:
    aliquota = 0.15
    deducao = 354.80

elif salario > 3751.06 & salario <= 4664.68:
    aliquota = 0.225
    deducao = 636.13

elif salario > 4664.68:
    aliquota = 0.275
    deducao = 869.36


calculoImposto = salario * aliquota - deducao
salarioFinal = salario - calculoImposto

print("Seu salario:", salario)
print("Imposto a pagar: ", calculoImposto)
print("Salario líquido", salarioFinal)