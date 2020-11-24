#Desafio 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sorted()). No final, mostre a lista ordenada na tela.

#RESOLUÇÃO PESSOAL : TERCEIRA TENTATIVA - Entendimento de 75% do exercício
lista_numeros = []

for valor in range(1,6):
    numeros = int(input(f'Digite o {valor}° valor: '))
    
    if valor == 1: #primeiro
        lista_numeros.append(numeros)
        print(f'{numeros} é o primeiro valor.')
    
    elif numeros > max(lista_numeros): #maior
        lista_numeros.append(numeros)
        print(f'{numeros} foi adicionado no final da lista')
    
    else:
        pos = 0
        while pos < len(lista_numeros):
            if numeros <= lista_numeros[pos]:
                lista_numeros.insert(pos, numeros)
                print(f' O {numeros} foi adicionado na lista')
                break
            pos=pos+1
            print(pos)
            
print(lista_numeros)



    


