'''
Meu projeto é apenas uma coleção de exercícios que aprendi em Python e reuni em um só lugar.
'''



# Inicio 
condicao = True
while condicao:
    entrada = input('Você quer "entrar" ou "sair"?: ').strip().lower()

    if entrada == 'entrar':
        os.system('cls')
        print('Você entrou no sistema!!\n')
        print('Vamos começar com algumas perguntas para criar seu perfil.\n')
        break  # Sai do primeiro loop e vai para o segundo
    elif entrada == 'sair':
        os.system('cls')
        print('Você saiu do sistema.')
        exit()  # Encerra o programa
    else:
        print('Você não digitou nem "entrar" nem "sair". Tente novamente!')  
        

while condicao: # Segundo loop: Pergunta as informações do usuário
    # confirmar as informações
    nome = input('Qual é o seu nome?: ')
    tamanho = len(nome)
    idade = int(input('Qual é a sua idade?: '))
    
    if not nome or not idade:  # Verifica se foi digitado algo válido
        os.system('cls')
        print("Você deixou campos vazios. Tente novamente!\n")
        continue  # Volta para o início do segundo loop
    idade = int(idade)
    ano_nascimento = 2025 - idade

# Exibe as informações
    print(f'\nAqui estão suas informações: Seu nome é {nome}, contem {tamanho} letras, você tem {idade} anos e nasceu em {ano_nascimento}.')
    print(f'\nOlá, {nome} seja bem-vindo(a) ao sistema!')
    
# Pergunta se as informações estão corretas
    while condicao:  # Loop que vai ficar perguntando até a resposta ser válida
        confirmacao = input('As informações estão corretas? (sim/não): ').strip().lower()
        if confirmacao == 'sim':
            os.system('cls')
            print('Obrigado! Saindo do programa...')
            exit()  # Sai do segundo loop
        elif confirmacao == 'não':
            os.system('cls')
            print('Vamos tentar novamente!\n')
            break  # Sai do loop de confirmação e volta para a parte de refazer as informações
        else:
            print('Resposta inválida. Por favor, responda com "sim" ou "não".')

