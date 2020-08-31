#Desafio 45: Crie um programa que faça o computador jogar jokenpô com você.

import random
from time import sleep

#RESOLUÇÃO PESSOAL
print('-=-'*30)
print('''Escolha uma opção:
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA ''')
print('-=-'*30)

opcao = int(input('Qual é a sua jogada? '))
if opcao == 0:
    jog = 'PEDRA'
elif opcao == 1:
    jog = 'PAPEL'
elif opcao == 2:
    jog = 'TESOURA'
else:
    print('JOGADA INVÁLIDA! TENTE NOVAMENTE.')
    exit()

sleep(0.5)
print('PEDRA...')
sleep(1)
print('PAPEL...')
sleep(1)
print('TESOURA!')
print('-=-'*30) 
sleep(0.5) 

lista1 = 'PEDRA PAPEL TESOURA'
l = lista1.split()

escolhapc = random.sample(l, 1)
print(f'Jogador escolheu {jog}. \nComputador escolheu {escolhapc[0]}. ')
if jog == escolhapc[0]:
    print('\033[37mEMPATE!\033[m')
elif (jog == 'PEDRA' and escolhapc[0] == 'TESOURA') or (jog == 'TESOURA' and escolhapc[0] == 'PAPEL') or (jog == 'PAPEL' and escolhapc[0] == 'PEDRA'):
    print('\033[32mVENCEU!\033[m')
else:
    print('\033[31mDERROTA!\033[m')