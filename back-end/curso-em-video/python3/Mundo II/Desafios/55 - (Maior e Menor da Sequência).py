#Desafio 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#EXERCÍCIO MARAVILHOSO 
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é de {maior}')
print(f'E o menor peso é de {menor}')

