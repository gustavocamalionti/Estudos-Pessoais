#Desafio 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 
# Ex: Digite um número: 1834 
#unidade: 4
#dezena: 3 
#centena: 8 
#milhar: 1

#MODO 01:
num = str(input('Digite um número de 0 a 9999: ')).strip()
num2 = (f'{num:0>4}')

print('Analisando...')
print(f'Unidade: {num2[-1]} ')
print(f'Dezena: {num2[-2]} ')
print(f'Centena: {num2[-3]} ')
print(f' Milhar: {num2[-4]} ')
print('-=-'*30)

#MODO 02:
num = str(input('Digite um número de 0 a 9999: ')).strip()
num2 ='0000' + num #Os 4 zeros irão ir sempre para a direita, garantindo as 4 posições iniciais.
print('Analisando:')
print(f'Unidade: {num2[-1]} ')
print(f'Dezena: {num2[-2]} ')
print(f'Centena: {num2[-3]} ')
print(f'Milhar: {num2[-4]} ')
print('-=-'*30)


#MODO 03: PROFESSOR
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando:')
print(f'Unidade: {u} ')
print(f'Dezena: {d} ')
print(f'Centena: {c} ')
print(f'Milhar: {m} ')
