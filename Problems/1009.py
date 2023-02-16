nome_vendedor = input()
salario = float(input())
vendas_mes = float(input())

def calcula_salario_com_bonus(salario, vensa_mes):
    return salario + (vendas_mes * 0.15)

print("TOTAL = R$ ", format(calcula_salario_com_bonus(salario,vendas_mes), '.2f'), sep='')