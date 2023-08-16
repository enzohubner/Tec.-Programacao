horasInicio = int(input("digite as horas de inicio"))
minutosInicio = int(input("digite os minutos de inicio"))
horasFim = int(input("digite as horas de termino"))
minutosFim = int(input("digite os minutos de termino"))

if horasInicio or horasFim > 24:
    print("Esse tempo de jogo nao é aceito")
elif minutosInicio or minutosFim > 59:
    print("esse tempo nao é aceito")


horaDeJogo = horasFim - horasInicio
minutosDeJogo = minutosFim - minutosInicio

print("Seu jogo comecou as ", horasInicio, "h e", minutosInicio, "min")
print("Seu jogo terminou ", horasFim, "h e", minutosFim, "min")
print("Tempo total de jogo: ", horaDeJogo, "h e", minutosDeJogo, "min")
