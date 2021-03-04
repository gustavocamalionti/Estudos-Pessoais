#Desafio 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('-'*20)
print('10 termos de uma PA')
print('-'*20)

p = int(input('Primeiro Termo: '))
r = int(input('Informe a razão: '))

for c in range(p, r*11, r):
    print(c, end='→')
print(f'\nEstá ai sua PA de razão {r}, começando no {p} e com o último termo sendo {p+r*10}. ')
