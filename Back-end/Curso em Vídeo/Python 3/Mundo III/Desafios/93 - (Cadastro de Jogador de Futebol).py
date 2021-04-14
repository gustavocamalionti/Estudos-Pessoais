#Desafio 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


#RESOLUÇÃO PESSOAL
jogador = {'Nome': str(input('Nome do Jogador: '))} 
partidas = []
soma_gols = 0

numero_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
for c in range(1, numero_partidas + 1):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    soma_gols = soma_gols + partidas[c-1]

jogador['gols'] = partidas
jogador['Total de Gols'] = soma_gols


#1° MÉTODO DE ESCRITA
print('-='*35)
print(jogador)
#2° MÉTODO DE ESCRITA
print('-='*35)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

#3° MÉTODO DE ESCRITA
print('-='*35)
print(f'O jogador {jogador["Nome"]} jogou {numero_partidas} partidas.')
for c in range(1, len(jogador["gols"])+1):
    print(f'=> Na partida {c}, fez {jogador["gols"][c-1]}')
print(f'Foi um total de {soma_gols} gols.')
print('-='*35)