#Desafio 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('-'*30)
print('JOGO DE PAR OU ÍMPAR')
print('-'*30)

escolha = ''

cont = 0
while True: 
    jogador = int(input('Qual número você escolhe? de 1 a 10: '))
    while jogador<1 or jogador>10:
        jogador = int(input('CARÁCTER INVÁLIDO!!! DIGITE UM NÚMERO ENTRE 1 E 10: '))
    escolha = str(input('PAR OU ÍMPAR? [P/I]: ')).upper().strip()[0]
    while escolha not in 'PIÍ':
        escolha = str(input('CARÁCTER INVÁLIDO!!! POR FAVOR, ESCOLHA ENTRE PAR OU ÍMPAR [P/I]: ')).upper().strip()[0]
        
    máquina = randint(1,10)
    soma = jogador + máquina
    if soma%2==0:
        if escolha == 'P':
            print(f'Você escolheu {jogador} e disse \033[32mPAR\033[m → Computador escolheu {máquina}. Total de {soma} \n{soma} É \033[32mPAR\033[m')
            print('\033[32mVOCÊ VENCEU!!!\033[m ')
            print('Vamos jogar novamente...')
            print('-=-'*30)
            cont = cont + 1
        else:
            print(f'Você escolheu {jogador} e disse \033[31mÍMPAR\033[m → Computador escolheu {máquina}. Total de {soma} \n{soma} É \033[31mPAR\033[m')
            print('\033[31mVOCÊ PERDEU!!!\033[m ')
            break
    elif soma%2!=0:
        if escolha == 'I':
            print(f'Você escolheu {jogador} e disse \033[32mÍMPAR\033[m → Computador escolheu {máquina}. Total de {soma} \n{soma} É \033[32mÍMPAR\033[m')
            print('\033[32mVOCÊ VENCEU!!!\033[m ')
            print('Vamos jogar novamente...')
            print('-=-'*30)
            cont = cont + 1
        else:
            print(f'Você escolheu {jogador} e disse \033[31mPAR\033[m → Computador escolheu {máquina}. Total de {soma} \n{soma} É \033[31mÍMPAR\033[m')
            print('\033[31mVOCÊ PERDEU!!!\033[m ')
            break
print('-=-'*30)
print(f'\033[35mGAMEOVER.\033[m Parabéns pela sequência de \033[32m{cont}\033[m vitórias!')
print('-=-'*30)

