sexo = float(input("digite o sexo: "))
peso = float(input("digite o peso: "))
altura = float(input("digite a altura em centimetros: "))
idade = float(input("digite a idade: "))

if sexo == "homen":
    calDiarias = 66 + (13.7*peso) + 5*altura - 6.8 * idade
elif sexo == "mulher":
    calDiarias = 665 + (9.6*peso) + 1.8*altura - 4.7* idade    