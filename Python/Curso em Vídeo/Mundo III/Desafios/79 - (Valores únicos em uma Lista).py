#Desafio 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele nõa será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

#RESOLUÇÃO PESSOAL
ee = ''
lista = []
while True:
    n = int(input('Digite um número: '))
    if lista.count(n)>1:
        e=0
    elif lista.count(n)<1:
        lista.append(n)

    quest = str(input('quer continuar? [S/N] ')).upper().strip()
    if quest == 'N' or quest == 'NÃO' or quest == 'NAO':
        break
    elif quest =='S' or quest == 'SIM':
        e = 0
    else:
        print('Digite um valor válido! \033[32mS!\033[m ou \033[31mN\033[m')
lista.sort()
print(f' {lista}')

#RESOLUÇÃO DO PROFESSOR
numeros = list()

while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com Sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar... ')

    r = str(input('Quer continuar? [S/N] ')).upper()
    if r in 'N':
        break

numeros.sort()
print(numeros)
