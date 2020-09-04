#052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#Resolução Pessoal
cont = 0
n = int(input('Digite um número: '))
for c in range(1,n+1): 
    if n%c==0: 
        cont = cont + 1 
        print(f'\033[32m{c}\033[m', end=' ')   
    else:
        print(f'\033[31m{c}\033[m', end=' ') 
print(f'\nO número {n} é divisível por outros {cont} números.')
if cont==2:
    print(f'{n} \033[32mÉ\033[m um número PRIMO.')
else:
    print(f'{n} \033[31mNÃO\033[m é um número PRIMO.')
    



