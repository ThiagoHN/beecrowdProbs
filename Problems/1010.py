def ler_converter_entrada():
    entrada = input().split()
    return int(entrada[0]),int(entrada[1]),float(entrada[2])

codigo_peça1, count_peça1, valor_peça1 = ler_converter_entrada()
codigo_peça2, count_peça2, valor_peça2 = ler_converter_entrada()

print("VALOR A PAGAR: R$ ", format((count_peça1 * valor_peça1) + (count_peça2 * valor_peça2), '.2f'), sep='')