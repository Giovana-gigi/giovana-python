
import os
os.system('cls') 

# """
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.
# """


numero = (input('Digite um valor: '))

if numero.isdigit():  # Verifica se o número é positivo
    numero = int(numero)

    if numero % 2 == 0: # par
        print(f"O número {numero} é par.")
    else: # caso nao seja o numero par ele vem aq
        print(f"O número {numero} é ímpar.")
else:
    print("Isso não é um número inteiro.")
    


