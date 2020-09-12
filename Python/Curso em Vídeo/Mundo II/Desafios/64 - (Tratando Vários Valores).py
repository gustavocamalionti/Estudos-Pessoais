#Desafio 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag).

#MÉTODO 1:
print('-'*30)
print('MÉTODO 1')
print('-'*30)

n = 0
cont = 0
soma = 0
while n!=999:
    n = int(input('Digite alguns valores inteiros [999 para parar]: '))
    cont = cont + 1
    soma = soma + n
print(f'Você digitou {cont-1} números e a soma entre eles vale {soma-999}.')

#MÉTODO 2:
print('-'*30)
print('MÉTODO 2')
print('-'*30)

n = 0
cont = 0
soma = 0
n = int(input('Digite alguns valores inteiros [999 para parar]: '))
while n!=999:
    cont = cont + 1
    soma = soma + n
    n = int(input('Digite alguns valores inteiros [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles vale {soma}.')