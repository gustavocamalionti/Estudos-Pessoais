#Desafio 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5!=5x4x3x2x1 = 120
#faça ele usando while e for.

from math import factorial


met1 = 'MÉTODO 1: USANDO [while]'
print(f'{met1:-^55}')
f = 1
num = int(input('Digite um número para calcular seu fatorial: '))
print(f'{num}! = ', end = '')
while num>0:
    print(num, end = '')
    f = f*num
    num = num - 1
    if num!=0:
        print('x', end = '')
    else:
        print('=',end = '')
print(f'{f}')


met2 = 'MÉTODO 2: USANDO [math]'
print(f'{met2:-^55}')
num = int(input('Digite um número para calcular seu fatorial: '))
print(f'{num}! = {factorial(num)}')


met3 = 'MÉTODO 3: USANDO [for]'
print(f'{met3:-^55}')

num = int(input('Digite um número para calcular seu fatorial: '))

f = 1
print(f'{num}! = ', end='')
for c in range(num, 0, -1):
    f = f*c
    print(c, end='')
    if c!=1:
        print('x', end='')
    else:
        print('=', end='')
print(f)
