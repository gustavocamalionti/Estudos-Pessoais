#Desafio 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: 
# A)Quantos números foram digitados. 
# B)A lista de valores, ordenada de forma decrescente. 
# C)Se o valor 5 foi digitado e está ou não na lista.

#RESOLUÇÃO PESSOAL: MANEIRA MAIS TRANQUILA USANDO sort(reverse=True).

cont5=0
cont=0
lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    cont=cont+1
    if n == 5:
        cont5=cont5+1

    quest = str(input('Quer continuar? [S/N] ')).upper().strip()
    if quest == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {cont} números')
print(f'O valor 5 apareceu {cont5} vezes')
print(lista)