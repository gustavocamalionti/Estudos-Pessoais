#Desafio 98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
# a) De 1 até 10, de 1 em 1 
# b) De 10 até 0, de 2 em 2 
# c) Uma contagem personalizada.

#Resolução Pessoal.

import time

def contagem(a, b, c, d):
    print('=-='*15)
    print(a)

    if a == msg_1:
        for z in range(b, c, d):
            print(z, end=' ')
        print()

    elif a == msg_2:
        cont = b
        while  cont>=0:
            print(cont, end=' ')
            cont = cont - d
        print()
    
    elif a == msg_3:
        if inicio < fim:
            for t in range(inicio, fim, passo):
                print(t, end=' ')
            print()

        else:
            cont2 = inicio 
            while cont2 >= fim:
                print(cont2, end=' ')
                cont2 = cont2 - passo
            print('')
    print('=-='*15)

msg_1 = 'Contagem de 1 até 10, de 1 em 1.'
msg_2 = 'Contagem de 10 até 0, de 2 em 2.'
msg_3 = 'Contagem personalizada'
contagem(a=msg_1, b = 1, c = 11, d = 1)
contagem(a=msg_2, b= 11, c = 0, d = 2)


print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(a=msg_3, b= inicio, c = fim, d = passo)