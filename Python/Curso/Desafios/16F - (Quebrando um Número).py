#Desafio 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. 
# Ex: Digite um número: 6.127. O número 6.127 tem a mesma parte inteira 6.

from math import trunc 

n = float(input('Digite um número: '))
print(f'O número {n} tem a parte inteira {trunc(n)} ')