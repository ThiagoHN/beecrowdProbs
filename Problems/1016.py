distancia = int(input())

def calcula_tempo(distancia):
    tempo = 0

    while distancia != 0:
        tempo += 2
        distancia -= 1
    
    return tempo

print(calcula_tempo(distancia), "minutos")