#Desafio 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

#MODO 01
met1 = 'PRIMEIRO MÉTODO' 
print('-'*30)
print(f'{met1:^30}')
print('-'*30)
maquinas = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)) 
print(maquinas)

print(f'{sorted(maquinas)[0]} é o menor valor')
print(f'{sorted(maquinas)[-1]} é o maior valor')

#MODO 02
met2 = 'SEGUNDO MÉTODO' 
print('-'*30)
print(f'{met2:^30}')
print('-'*30)
maquinas = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)) 
print(maquinas)

print(f'{min(maquinas)} é o menor valor')
print(f'{max(maquinas)} é o maior valor')