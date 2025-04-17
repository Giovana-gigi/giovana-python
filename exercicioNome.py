"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
       - Seu nome é {nome}
       - Seu nome invertido é {nome invertido}
        - Seu nome contém (ou não) espaços
       - Seu nome tem {n} letras
       - A primeira letra do seu nome é {letra}
       -  A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""





# solicite o nome e a idade do usuáio
nome = input('Qual é o seu nome?: ').strip()
idade = input('Qual é a sua idade?: ').strip()
# Processa as informações do nome 
nome_invertido = nome[::-1]
quantidade_de_letras = len(nome)
tem_espacos = 'TEM espaços' if ' ' in nome else 'NÃO contem espaço'
encontrar = input('Digite o que deseja encontrar: ').strip()
  
# Verifica se o nome ou a idade estão vazios
if not nome or not idade or not encontrar:
    print('Desculpe, você deixou campos vazios.')

else: #O else serve para executar um código quando a condição do if for falsa.
    # Processa as informações do nome 
    primeira_letra = nome[0]  #Se o nome estiver vazio, acessar nome[0] ou nome[-1]
    ultima_letra = nome[-1]  #resultaria em um erro do tipo IndexError, porque não há caracteres na string
    # Solicita o que o usuário deseja encontrar no nome
    print(f'Seu nome invertido é ({nome_invertido})')
    print(f'Seu nome {tem_espacos}')
    print(f'Seu nome tem {quantidade_de_letras} quantidade de letras')
    print(f'A primeira letra do seu nome é ({primeira_letra})')
    print(f'A ultima letra do seu nome é ({ultima_letra})')


    # Verifica se o termo está no nome
    if encontrar in nome:
        print(f'{encontrar} foi encontrado no nome.')
    else:
        print(f'{encontrar} não foi encontrado')

