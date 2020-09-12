#Desafio 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. 

maior = menor = soma = cont = 0
continuar = ''
while continuar in 'S':
    n = int(input('Digite alguns valores inteiros: '))
    soma = soma + n
    cont = cont + 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n>maior:
            maior = n
        if n<menor:
            menor = n
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma/cont
print('Obrigado!')
print(f'Você digitou {cont} valores e a média entre eles vale {media}. Além disso, o maior valor é {maior} e o menor é {menor}.')

