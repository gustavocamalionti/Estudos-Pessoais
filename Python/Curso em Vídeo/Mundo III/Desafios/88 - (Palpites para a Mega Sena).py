#Desafio 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntas quantos jogos serão gerados e vai sortear 6 números entre 1 e 60, para cada jogo, cadastrando tudo em uma lista composta.

#RESOLUÇÃO PESSOAL 
import random 

cartela = []
jogos = []
titulo = 'JOGO DA MEGA SENA'
print('-'*30)
print(f'{titulo:^30}')
print('-'*30)

quantidade_jogos = int(input('Qual a quantidade de jogos? '))

for numbers in range(1,61):
    cartela.append(numbers)

for c in range(0, quantidade_jogos):
    dados = random.sample(cartela, 6)
    jogos.append(dados[:])
    dados.clear()
    print(f'Jogo {c+1}: {jogos[c]}')