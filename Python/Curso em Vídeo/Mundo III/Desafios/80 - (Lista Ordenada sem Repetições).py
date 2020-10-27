#Desafio 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


#RESOLUÇÃO DO PROFESSOR: REVISAR!
numeros = list()
for c in range(0,5):
    n = int(input(f'Digite o {c+1}° número: '))
    if c==0 or n>numeros[-1]:
        numeros.append(n)
        print(f'O valor {n} foi adicionado no final da lista')

    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'O valor {n} foi adicionado na posição {pos}')
                break
            else:
                pos = pos + 1
        
print(numeros)

#RESOLUÇÃO DE UM AMIGO: REVISAR.
lista = list()
for c in range(5):
    n = int(input("Digite o numero: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        for pos, x in enumerate(lista):
            if n <= x:
                lista.insert(pos, n)
                break
print(lista)

#RESOLUÇÃO PESSOAL - PRIMEIRA TENTATIVA