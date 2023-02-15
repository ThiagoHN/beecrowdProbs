import math

def ler_converter_entrada():
    entrada = input().split()
    return [float(entrada[0]),float(entrada[1])]

ponto1 = ler_converter_entrada()
ponto2 = ler_converter_entrada()
print(format(math.dist(ponto1,ponto2), '.4f'))