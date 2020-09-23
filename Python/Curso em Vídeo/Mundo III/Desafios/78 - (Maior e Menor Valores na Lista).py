#Desafio 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

#RESOLUÇÃO PESSOAL
numeros = []

for c in range(0,5):
    numeros.append(int(input(f'Digite o {c}° número: ')))
print(numeros)

print(f'O maior valor vale {max(numeros)} e está nas posições ', end = '')
for c,v in enumerate(numeros):
    if v == max(numeros):
        print(c, end = '...')

print(f'O menor valor vale {min(numeros)} e está nas posições ', end = '')
for c,v in enumerate(numeros):
    if v == min(numeros):
        print(c, end = '...')
print('FIM!')

#RESOLUÇÃO DO PROFESSOR
maior = 0
menor = 0

numeros = []
for c in range(0,5):
    numeros.append(int(input(f'Digite o {c}° número: ')))
    if c==0:
        maior = numeros[c]
        menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]

print('-'*40)
print(f'Você digitou: {numeros}')


print(f'O Maior valor vale {maior} nas posições ', end='')
for c,v in enumerate(numeros):
    if v == maior:
        print(c, end='...')

print(f'\nO Menor valor digitado vale {menor} nas posições ', end='')
for c,v in enumerate(numeros):
    if v == menor:
        print(c, end='...')
print('\n FIM!')


