#Desafio 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 
# Ex: Digite um número: 1834 
#unidade: 4
#dezena: 3 
#centena: 8 
#milhar: 1


n = str(input('Digite um número entre 0 a 9999:'))

print(f'unidade: {n[3]:}')