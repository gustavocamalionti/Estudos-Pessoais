#Desafio 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []

for c in range(0,5):
    numeros.append(int(input(f'Digite o {c}° número: ')))
print(f'Você digitou: {numeros}')
print(f'O Menor valor vale {min(numeros)} na posição {numeros.index(min(numeros))} e o maior valor vale {max(numeros)} na posição {numeros.index(max(numeros))} ')
