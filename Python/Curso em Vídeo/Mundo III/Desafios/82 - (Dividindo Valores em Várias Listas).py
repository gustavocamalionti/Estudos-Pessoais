#Desafio 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo dos três listas geradas.

#RESOLUÇÃO PESSOAL
lista = []
impares = []
pares = []
while True:
    n = int(input('Digite um valor inteiro: '))
    lista.append(n)
    if n%2==0:
        pares.append(n)
    else: 
        impares.append(n)

    quest = str(input('Quer continuar? [S/N] ')).strip().upper()
    if quest == 'N':
        break

print(f'Conjunto com os valores: {lista}')
print(f'Subconjunto com os valores impares: {impares}')
print(f'Subconjunto com os valores pares: {pares}')

