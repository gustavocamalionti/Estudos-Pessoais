#Desafio 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

#RESOLUÇÃO PESSOAL - PRIMEIRA TENTATIVA

primeirovalor = 0
cont = 0
lista = []
for c in range(5):
    n = int(input('Digite um número: '))
    if cont == 0:
        lista.append(n)
    
    elif cont != 0:
        for c in lista:
            if min(lista)<n:
                lista.append(n)
                print(f' O valor {n} foi adicionado no final da lista')
            

    cont = cont+ 1
print(lista)
    