mes = int(input("digite um mes: "))
ano = int(input("digite um ano"))

if ano % 4 == 0:
    print("ano bissexto")
    if mes == 2:
        print("O mes tem 29 dias")
    elif mes % 2 == 0:
        print("Seu mes tem 30 dias")
    else:
        print("Seu mes tem 31 dias")

else:
    print("ano regular")
    if mes == 2:
        print("O mes tem 28 dias")
    elif mes % 2 == 0:
        print("Seu mes tem 30 dias")
    else:
        print("Seu mes tem 31 dias")