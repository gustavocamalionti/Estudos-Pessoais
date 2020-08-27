#Desafio 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 
# Ex: Digite um número: 1834 
#unidade: 4
#dezena: 3 
#centena: 8 
#milhar: 1

num = str(input('Digite um número de 0 a 9999: ')).strip()
num2 = (f'{num:0>4}')

print('Analisando...')
print(f'Unidade: {num2[3]} ')
print(f'Dezena: {num2[2]} ')
print(f'Centena: {num2[1]} ')
print(f' Milhar: {num2[0]} ')