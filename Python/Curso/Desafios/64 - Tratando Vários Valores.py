#Desafio 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag).

n = 0
cont = 0
soma = 0
while n!=999:
    n = int(input('Digite alguns valores inteiros: '))
    cont = cont + 1
    soma = soma + n
print(f'Você digitou {cont-1} números e a soma entre eles vale {soma-999}.')

