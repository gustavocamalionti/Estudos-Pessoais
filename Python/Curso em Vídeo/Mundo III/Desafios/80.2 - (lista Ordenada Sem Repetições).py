#Desafio 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

#RESOLUÇÃO PESSOAL - PRIMEIRA TENTATIVA
pos = 0
lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    #situação 1: Primeiro Valor
    if c == 0:
        lista.append(n)
        print(f'Foi adicionado {n}, é o primeiro valor. ')
    
    #situação 2: Maior valor
    elif n > lista[len(lista)-1]: #elif n>lista[-1]:
        lista.append(n)
        print(f'Foi adicionado {n} no final da lista. ')
    
    #situação 3: valor intermediario
    else:
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break

            pos = pos+1

print(lista)
    