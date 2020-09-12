#Desafio 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

a = str(input('Digite o nome do aluno A: '))
b = str(input('Digite o nome do aluno B: '))
c = str(input('Digite o nome do aluno C: '))
d = str(input('Digite o nome do aluno D: '))
lista = [a, b, c, d]
escolhido = random.choice(lista)
print(f'Sorteando um aluno dos 4 da sala, o {escolhido} foi escolhido! ')