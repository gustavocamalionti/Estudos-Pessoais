#Desafio 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.

#RESOLUÇÃO PESSOAL

dados = []
pessoas_grupo = []
pessoas_peso = [[], []]
menu_resposta = ''
peso_maior = peso_menor = 0
contagem_pessoas = 0
import time 

while True: 
    nome_usuario = str(input('Digite seu nome: ')).upper().strip()
    dados.append(nome_usuario)
    peso_usuario = float(input('Digite seu peso: '))
    if contagem_pessoas == 0:
        peso_maior = peso_menor = peso_usuario
    else:
        if peso_usuario > peso_maior:
            peso_maior =  peso_usuario
        elif peso_usuario < peso_menor:
            peso_menor = peso_usuario
            
    dados.append(peso_usuario)
    pessoas_grupo.append(dados[:])
    contagem_pessoas = contagem_pessoas + 1
    dados.clear()

    menu_resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
    while menu_resposta not in 'SN':
        print('Resposta Inválida,',end='')
        menu_resposta = str(input(' Tente novamente. Quer continuar? [S/N] ')).upper().strip()

    if menu_resposta == 'N':
        break
    
    for c in range(0, len(pessoas_grupo)):
        print(c)



print(peso_maior)
print(peso_menor)
print(pessoas_grupo)
print(contagem_pessoas)
print(pessoas_peso)




