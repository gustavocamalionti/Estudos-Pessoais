#Desafio 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele nõa será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

#Resolução do Professor




#Resolução Pessoal
ee = ''
quest = '0'
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
