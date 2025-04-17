import os
os.system('cls') 


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


horario = input("Que horas são?: ")

try: #tentar executar um código
    horario = int(horario)
    if 0 <= horario <= 11:
        print(f'Bom Dia, são {horario}h da manhã!')
    elif 12 <= horario <= 17:
        print(f'Boa tarde, são {horario}h da tarde!')
    elif 18 <= horario <= 23:
        print(f'Boa noite, são {horario}h! da noite')
    else:
        print('Não conheço esse horario')

except: # se ocorreu algum erro ao tentar executar um cósigo
    print("Por favor, insira um número inteiro válido para o horário.")
