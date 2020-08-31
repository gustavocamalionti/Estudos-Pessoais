#Desafio 45: Crie um programa que faça o computador jogar jokenpô com você.

import random
from time import sleep

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

lista1 = 'PEDRA PAPEL TESOURA'
l = lista1.split()

escolhapc = random.sample(l, 1)
print(f'Jogador escolheu {jog}. \nComputador escolheu {escolhapc[0]}. ')
if (jog == 'PEDRA' and escolhapc == 'PEDRA') or (jog == 'TESOURA' and escolhapc == 'TESOURA') or (jog == 'PAPEL' and escolhapc == 'PAPEL'):
    print('EMPATE')

