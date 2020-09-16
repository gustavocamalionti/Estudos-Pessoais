#Desafio 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


numext = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um número de 0 até 20: '))
    while n<0 or n>20:
        n = int(input('TENTE NOVAMENTE. Digite um número de 0 até 20: '))
    print(f'Você digitou o número \033[32m{numext[n]}\033[m')

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break    
print('Muito Obrigado!')
