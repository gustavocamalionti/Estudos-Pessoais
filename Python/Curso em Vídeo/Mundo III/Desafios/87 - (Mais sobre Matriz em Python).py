#Desafio 87: Aprimore o exercício anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna. 
# C) O maior valor da segunda linha

#RESOLUÇÃO PESSOAL
soma_pares = 0
soma_coluna = 0
maior_segunda_linha = []
matriz = [[],[],[]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha].append(int(input(f'Digite um valor para [{linha+1},{coluna+1}] ')))
        if matriz[linha][coluna]%2==0:
            soma_pares = soma_pares + matriz[linha][coluna]
        elif linha == 1:
            maior_segunda_linha.append(matriz[1][coluna])

    soma_coluna = soma_coluna + matriz[linha][2]


print('-='*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-='*30)

print(f'A soma dos valores pares: {soma_pares} ')
print(f'A soma dos valores da terceira coluna: {soma_coluna} ')
print(f'O maior valor da segunda linha: {max(maior_segunda_linha)} ')