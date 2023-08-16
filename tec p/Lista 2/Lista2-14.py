horasInicio = int(input("digite as horas d inicio: ")) 
minutosInicios = int(input("digite os minutos de inicio: "))

horasFIm = int(input("digite as horas d termino ")) 
minutosFim = int(input("digite os minutos de termino: "))

calcTempoHoras = horasInicio - horasFIm
if calcTempoHoras < 0:
    calcTempoHoras = -calcTempoHoras

calcTempoMinuto = minutosInicios - minutosFim
if calcTempoMinuto < 0:
    calcTempoMinuto = -calcTempoMinuto

print("inicio do jogo", horasInicio, "h", minutosInicios, "min")
print("fim do jogo", horasFIm, "h", minutosFim, "min")
print("duração: ", calcTempoHoras, "h", calcTempoMinuto, "min")