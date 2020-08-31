#Desafio 038: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: 
# - O primeiro valor é maior. 
# - O segundo valor é maior.
# - Não existe valor maior, os dois são iguais.

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

if a>b:
    print('O primeiro valor é MAIOR. ')
elif b>a:
    print('O segundo valor é MAIOR. ')
else:
    print('Os valores são IGUAIS. ')