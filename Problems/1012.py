entrada = input().split()
A = float(entrada[0]) 
B = float(entrada[1]) 
C = float(entrada[2]) 

def area_triangulo_retangulo(A,C):
    return A * C / 2

def area_circulo(C):
    return 3.14159 * (C ** 2)

def area_trapezio(A,B,C):
    return (A + B) * C / 2

def area_quadrado(B):
    return B ** 2

def area_retangulo(A,B):
    return A * B

print(
        "TRIANGULO: ",format(area_triangulo_retangulo(A,C),'.3f'),
        "\nCIRCULO: ",format(area_circulo(C),'.3f'),
        "\nTRAPEZIO: ",format(area_trapezio(A,B,C),'.3f'),
        "\nQUADRADO: ",format(area_quadrado(B),'.3f'),
        "\nRETANGULO: ",format(area_retangulo(A,B),'.3f'), sep=''
    )