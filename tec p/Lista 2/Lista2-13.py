hasteAco = int(input("digite a quantidade de hastes de aco"))/3
hasteCobre = int(input("digite a quantidade de hastes de cobre: "))/3
hasteAl = int(input("digite a quantidade de hastes de aluminio: "))/3

total = hasteAco*2.5 + hasteCobre*4 + hasteAl*5
quantTotal = hasteAco + hasteCobre + hasteAl

if quantTotal < 6:
    desc = 0
if 7 <= quantTotal <= 15:
    desc = 0.1
if 16 <= quantTotal <= 20:
    desc = 0.15
if quantTotal > 20:
    desc = 0.2

valorTotal = total - total*desc

print(valorTotal)