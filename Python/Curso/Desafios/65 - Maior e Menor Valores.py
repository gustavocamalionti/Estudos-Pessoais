#Desafio 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. 


cont = 0
soma = 0
n = 0
menor = maior = n
while n!=999:
    n = int(input('Digite alguns valores inteiros: '))
    if n!=999:
        cont = cont + 1
        soma = soma + n
        media = (soma)/(cont)
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Obrigado!')
print(f'Você digitou {cont} valores e a média entre eles vale {media}. Além disso, o maior valor é {maior} e o menor é {menor}.')

