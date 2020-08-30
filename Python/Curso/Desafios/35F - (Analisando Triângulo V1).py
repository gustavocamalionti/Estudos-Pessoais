#Desafio 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.


from math import sqrt
print('-=-'*20)
print('Um triângulo nem sempre vai existir! bora ver esses casos então.')
print('-=-'*20)
a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))

if a<(b+c) and b<(a+c) and c<(a+b):
    print('O triângulo existe com os seguimentos acima.')
else:
    print('O triângulo não existe com esses segmentos.')

