#Desafio 020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem deles

import random

a = str(input('Digite o nome do primeiro representante: '))
b = str(input('Digite o nome do segundo representanto: '))
c = str(input('Digite o nome do terceiro representante: '))
d = str(input('Digite o nome do Quarto representante:'))

lista = [a, b, c, d]
emb = random.sample(lista, 3)


print(f'A sequência de apresentação dos grupos será: {emb}')