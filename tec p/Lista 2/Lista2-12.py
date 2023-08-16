sexo = int(input("digite o sexo: "))
idade = int(input("digite a idade: "))

if sexo == "homem" and idade > 21:
    print("Voce é maior idade")
elif sexo == "mulher" and idade > 18:        
    print("Voce é maior de idade")