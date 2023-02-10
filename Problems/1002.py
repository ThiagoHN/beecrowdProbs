def cal_area_circulo(raio):
    area = ((raio ** 2) * 3.14159)
    print("A=",format(area, '.4f'), sep='')

raio = float(input())
cal_area_circulo(raio)