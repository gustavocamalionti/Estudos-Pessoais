#Desafio 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número inteiro: '))
if n%2==1:
    print('O número é IMPAR.')
else: 
    print('O número é PAR.')