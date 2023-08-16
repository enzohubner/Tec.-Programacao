alturaAzulejo = float(input("Digite a altura do azulejo: "))
larguraAzulejo = float(input("Digite a largura do azulejo: "))

alturaParede = float(input("Digite a altura da parede: "))
larguraParede = float(input("Digite a largura da parede: "))

azulejosVerticais = alturaParede/alturaAzulejo
azulejosHorizontais = larguraParede/larguraAzulejo

qntdTotal = azulejosVerticais * azulejosHorizontais
print(qntdTotal)