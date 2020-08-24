#Desafio 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digita algo ai, fazendo favor: ')
print('é um número?:', n.isnumeric())
print('é uma palavra ou letra?:', n.isalpha())
print('Possui só letras maiúsculas?', n.islower())