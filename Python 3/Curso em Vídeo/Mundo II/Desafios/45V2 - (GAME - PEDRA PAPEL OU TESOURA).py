#RESOLUÇÃO DO PROFESSOR/LEONARDO:
from time import sleep
import random
print('''Escolha uma opção:
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA ''')
print('-=-'*30)

jog = int(input('Qual é a sua jogada? '))
if jog<0 or jog>2:
    print('COMANDO INVÁLIDO, TENTE NOVAMENTE')
    exit()
sleep(0.5)
print('PEDRA...')
sleep(1)
print('PAPEL...')
sleep(1)
print('TESOURA!')
print('-=-'*30) 
sleep(0.5) 

itens = ['PEDRA', 'PAPEL', 'TESOURA']
pc = random.randint(0,2)

print(f'Jogador escolheu {itens[jog]}. \nComputador escolheu {itens[pc]}. ')
if jog==pc:
    print('EMPATE!')
elif (jog<2 and pc==jog+1) or (pc==0 and jog==2):
    print('DERROTA!')
else:
    print('VITÓRIA!')
print('-=-'*30)
