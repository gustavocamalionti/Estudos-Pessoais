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


while True: 
    nome_usuario = str(input('Digite seu nome: ')).upper().strip()
    dados.append(nome_usuario)
    peso_usuario = float(input('Digite seu peso: '))
    dados.append(peso_usuario)
    pessoas_grupo.append(dados[:])
    dados.clear()
    contagem_pessoas = contagem_pessoas + 1

    if contagem_pessoas == 1:
        peso_maior = peso_menor = peso_usuario
    else:
        if peso_usuario > peso_maior:
            peso_maior =  peso_usuario
        elif peso_usuario < peso_menor:
            peso_menor = peso_usuario
            

    menu_resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
    while menu_resposta not in 'SN':
        print('Resposta Inválida,',end='')
        menu_resposta = str(input(' Tente novamente. Quer continuar? [S/N] ')).upper().strip()

    if menu_resposta == 'N':
        break
    
for c in range(0, len(pessoas_grupo)):
    if pessoas_grupo[c][1] > peso_maior:
        pessoas_peso[0].clear()
        pessoas_peso[0].append(pessoas_grupo[c])
        
    elif pessoas_grupo[c][1] == peso_maior:
        pessoas_peso[0].append(pessoas_grupo[c])
            
    elif pessoas_grupo[c][1] < peso_menor:
        pessoas_peso[1].clear()
        pessoas_peso[1].append(pessoas_grupo[c])
        
    elif pessoas_grupo[c][1] == peso_menor:
        pessoas_peso[1].append(pessoas_grupo[c])

print(f'Foi adicionado \033[32m{contagem_pessoas}\033[m usuários no sistema.')
print('As pessoas mais leves são: ', end='')
for c in range(0,len(pessoas_peso[1])):
    print(pessoas_peso[1][c][0], end='...')

print('\nAs pessoas mais pesadas são: ', end='')
for c in range(0,len(pessoas_peso[0])):
    print(pessoas_peso[0][c][0], end='...')

#RESOLUÇÃO PROFESSOR:
print('\n', '-=-'*25)

dados = []
pessoas_grupo = []
menu_resposta = ''
peso_maior = peso_menor = 0

while True: 
    dados.append(str(input('Digite seu nome: ')).upper().strip())
    dados.append(float(input('Digite seu peso: ')))
    if len(pessoas_grupo) == 0:
        peso_maior = peso_menor = dados[1]
    else:
        if dados[1] > peso_maior:
            peso_maior = dados[1]
        elif dados[1] < peso_menor:
            peso_menor = dados[1]

    pessoas_grupo.append(dados[:])
    dados.clear()

    menu_resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
    while menu_resposta not in 'SN':
        print('Resposta Inválida,',end='')
        menu_resposta = str(input(' Tente novamente. Quer continuar? [S/N] ')).upper().strip()
     
    if menu_resposta == 'N':
        break

print(f'Ao todo, você cadastrou {len(pessoas_grupo)}')
print(f'O maior peso foi de {peso_maior}. Peso de ', end='')
for p in pessoas_grupo:
    if p[1] == peso_maior:
        print(f'{p[0]}', end='...')

print(f'\nO menor peso foi de {peso_menor}. Peso de ', end='')
for p in pessoas_grupo:
    if p[1] == peso_menor:
        print(f'{p[0]}', end='...')

