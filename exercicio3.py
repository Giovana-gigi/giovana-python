"""
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual seu nome?: ').strip()
tamanho = len(nome)


if tamanho <= 4 and nome.isalpha():
    print(f'Seu nome é curto, ele contém {tamanho} letras')
   
elif 5 <= tamanho <= 6 and nome.isalpha():
    print(f'Seu nome é normal, e contem {tamanho} letras')

elif tamanho > 6 and nome.isalpha():
    print(f'Seu nome é muito grande, e contem {tamanho} letras')
   
else:
    print('Isso não são letras, por favor digite um nome')
