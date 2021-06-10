#Desafio 86: crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

#RESOLUÇÃO PESSOAL
matriz = [[],[],[]]

for c in range(1,4):
    if 0<=c<=3:
        matriz[c-1].append(int(input(f'Digite um valor para [{c},{1}]: ')))
        matriz[c-1].append(int(input(f'Digite um valor para [{c},{2}]: ')))
        matriz[c-1].append(int(input(f'Digite um valor para [{c},{3}]: ')))
    else:
        break

for z in range(0,3):
    print(f'[ {matriz[z][0]:^5} ]', end='')
    print(f'[ {matriz[z][1]:^5} ]', end='')
    print(f'[ {matriz[z][2]:^5} ]')

#RESOLUÇÃO DO PROFESSOR
matriz = [[],[],[]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha].append(int(input(f' Digite um valor para [{linha+1},{coluna+1}] ')))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
    

