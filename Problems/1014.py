distancia_total = int(input())
combustivel_gasto = float(input())

def consumo_medio_automavel(distancia_total,combustivel_gasto):
    return distancia_total/combustivel_gasto

print(format(consumo_medio_automavel(distancia_total,combustivel_gasto),'.3f'), " km/l", sep='')