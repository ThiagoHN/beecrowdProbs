num_funcionario = int(input()) 
horas_trabalho = int(input())
valor_hora = float(input())

def calc_salario(horas_trabalho, valor_hora):
    return horas_trabalho * valor_hora

print("NUMBER = ",num_funcionario, 
      "\nSALARY = U$ ", format(calc_salario(horas_trabalho,valor_hora), '.2f'), sep='')