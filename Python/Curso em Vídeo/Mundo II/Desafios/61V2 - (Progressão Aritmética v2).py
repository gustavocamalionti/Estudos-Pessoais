#Desafio 061: Refaça o desafio 051, lendo o primeiro termo e a razão de uma pa, mostrando os 10 primeiros termos da progressão usando a estrutura while.

#RESOLUÇÃO DO PROFESSOR
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo} ', end = '')
    termo = termo + razao
    cont = cont + 1
print('FIM')

