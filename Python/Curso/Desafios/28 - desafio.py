#Desafio 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. #O programa deverá escrever na tela se o usuário venceou ou perdeu.

print('-=-'*22)
print('Acabei de pensar em um número entre "0" e "5". Tente adivinhar...')
print('-=-'*22)

import time #impressão de tempo passando com a função sleep
import random #from random import randint
pc = random.randint(0,5) #computador = randint(0,5) >>>>>>>>>>>>>> #esse comando faz o computador "Pensar"


jog = int(input('Qual número você escolhe? '))
print('Processando...')
time.sleep(3)
if jog == pc:
    print('Parabéns, fui vencido!')
else:
    print(f'Lamento, você perdeu! Pensei no {pc} e você arriscou {jog}.')