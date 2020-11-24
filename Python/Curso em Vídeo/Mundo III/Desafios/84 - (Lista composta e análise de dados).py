#Desafio 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.

#RESOLUÇÃO PESSOAL

dados = []
pessoas_grupo = []
menu_resposta = ''

import time 

while True: 
    nome_usuario = str(input('Digite seu nome: '))
    dados.append(nome_usuario)
    peso_usuario = float(input('Digite seu peso: '))
    dados.append(peso_usuario)
    pessoas_grupo.append(dados[:])
    dados.clear()

    menu_resposta = str(input('Quer continuar? [S/N]')).upper().strip()
    while menu_resposta not in 'SN':
        print('Resposta Inválida,',end='')
        menu_resposta = str(input(' Tente novamente. Quer continuar? [S/N]')).upper().strip()

    if menu_resposta == 'N':
        break
    

    

print('teste')





