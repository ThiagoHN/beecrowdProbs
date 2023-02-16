raio = float(input())

def calc_vol_esfera(raio):
    return (4/3) * 3.14159 * (raio ** 3)

print("VOLUME = ", format(calc_vol_esfera(raio), '.3f'), sep='')