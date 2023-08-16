carrosVendidos = float(input("Declare a quantidade de carros vendidos:"))
valorVendas = float(input("Declare o valor de vendas:"))
salarioFixo = float(input("Declare o salario fixo:"))
comissao = float(input("Declare o valaro de comissao:"))

salarioFinal = salarioFixo + comissao * carrosVendidos + (5*valorVendas/100)
print(salarioFinal)