#Desafio 059: Crie um programa que leia dois valores e mostre um menu na tela: 
# [1] Somar 
# [2] Multiplicar 
# [3] Maior 
# [4] Novos números 
# [5] Sair do programa 
# Seu programa deverá realizar a operação solicitada em casa caso.

import time

n1 = float(input('Escolha um número: '))
n2 = float(input('Escolha outro número: '))

maior = 0
menor = 0
num = 0

print('-'*35)
while num != 5:
    num = int(input('[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA \nEscolha uma das opções acima: '))
    if num == 1:
        print(f'A SOMA entre \033[31m{n1}\033[m e \033[31m{n2}\033[m vale \033[32m{n1+n2}\033[m')
        print('-'*35)
        time.sleep(1)
    elif num == 2:
        print(f'A MÚLTIPLICAÇÃO entre \033[31m{n1}\033[m e \033[31m{n2}\033[m vale \033[32m{n1*n2}\033[m')
        print('-'*35)
        time.sleep(1)
    elif num == 3:
        if n1>n2:
            maior=n1
        if n2>n1:
            maior=n2
        print(f'Entre \033[31m{n1}\033[m e \033[31m{n2}\033[m, o maior número vale \033[32m{maior}\033[m ')
        print('-'*35)
        time.sleep(1)
    elif num == 4:
        time.sleep(1)
        n1 = float(input('Escolha um número: '))
        n2 = float(input('Escolha outro número: '))
        print('-'*35)
        time.sleep(1)
    elif num>5 or num<1:
        print('\033[31mOpção INVÁLIDA!\033[m tente novamente. ')
        print('-'*35)
        time.sleep(1)
time.sleep(1)
print('\033[32mOBRIGADO!\033[m Fim do programa.')