#Desafio 4.1: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele de outra forma, utilizando o conceito de {} visto na aula teórica de tipos primitivos.

n = input('Digita algo ai, fazendo favor: ') 
print(f'O tipo primitivo de {n} é: {type(n)}')
print(f'"{n}" é um número?: {n.isnumeric()}')
print(f'"{n}" é uma palavra ou letra?: {n.isalpha()}') 
print(f'"{n}" possui só letras minúsculas? {n.islower()}')
print(f'"{n}" possui só letras maiúsculas? {n.isupper()}')
print(f'"{n}" seria um número alfanumérico? {n.isalnum()}')
print(f'"{n}" tem apenas espaços? {n.isspace()}')
print(f'"{n}" está capitalizada? {n.istitle()}')