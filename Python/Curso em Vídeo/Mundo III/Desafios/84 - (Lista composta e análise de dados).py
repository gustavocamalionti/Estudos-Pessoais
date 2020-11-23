#Desafio 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.

#RESOLUÇÃO PESSOAL
dados = []
grupo_pessoas = []
pesos_lista = [[], []]
cont=0
contagem_pessoas = 0
maior=menor=0

while True:
    nome = str(input('Nome: ')).strip()
    dados.append(nome)

    peso = float(input('Peso: '))
    dados.append(peso)

    contagem_pessoas = contagem_pessoas + 1
    grupo_pessoas.append(dados[:])
    dados.clear()

    parar_programa = str(input('Deseja parar? [S/N] ')).upper()
    if parar_programa == 'S':
        break

for c in range(0,len(grupo_pessoas)):
    if grupo_pessoas[c][1] >= maior:
        pesos_lista[0].append(grupo_pessoas[c])
    elif grupo_pessoas[c][1] <= menor:
        pesos_lista[1].append(grupo_pessoas[c])

print(f'{grupo_pessoas}')
print(f'{pesos_lista}')
