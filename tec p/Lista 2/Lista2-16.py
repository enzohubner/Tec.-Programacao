num = int(input("digite um algarismo de tres digitos: "))
num2 = num%100
soma = num//100 + num2%10 + num2//10
print("a soma dos algarismo do numero é: ", soma)



if num%4 == 0 and 16%num == 0:
    print("o numero é multiplo de 4 e divisor de 16")