#Desafio 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digita algo ai, fazendo favor: ') 
print('O tipo primitivo dele é:', type(n))
print('É um número?:', n.isnumeric())
print('É uma palavra ou letra?:', n.isalpha())
print('Possui só letras minúsculas?', n.islower())
print('Possui só letras maiúsculas?', n.isupper())
print('Seria um número alfanumérico?', n.isalnum())
print('só existe espaços?', n.isspace())
print('Ela está capitalizada?', n.istitle())