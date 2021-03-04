#Desafio 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. 

#RESOLUÇÃO DO PROFESSOR: ENTENDIMENTO DE 75% - REVISAR
from random import randint
from time import sleep
from operator import itemgetter


jogadores = {'jogador 1': randint(1,6),
             'jogador 2': randint(1,6),
             'jogador 3': randint(1,6),
             'jogador 4': randint(1,6)}

ranking = []

print('Valores sorteados')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.35)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking)


text = 'RANKING DOS JOGADORES '
print('-='*15)
print(f'{text:^30}')
print('-='*15)

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar:{v[0]} com {v[1]} pontos.')
    sleep(0.35)
