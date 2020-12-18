#Desafio 94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A)Quantas pessoas foram cadastradas 
# B) A média de idade do grupo. 
# C) Uma lista com todas as mulheres. 
# D) Uma lista com todas as pessoas com idade acima da média. 


#RESOLUÇÃO PESSOAL 
soma_pessoas = 0
soma_numerador = 0
continuar = ''
agrupamento_pessoas = []
contador = 0
while True: 
    pessoas = {'Nome': str(input('Nome: ')),'Sexo': str(input('Sexo [M/F] ')).strip().upper()}
    while pessoas['Sexo'] not in  'MF':
        pessoas['Sexo'] = str(input('Resposta incorreta! Qual seu sexo? [M/F] ')).strip().upper()
    pessoas['Idade'] = int(input('Idade: '))
    agrupamento_pessoas.append(pessoas)
    soma_pessoas = soma_pessoas + 1

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'S/N':
        continuar = str(input('Resposta incorreta! Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

for c in range(0, len(agrupamento_pessoas)):
    soma_numerador = soma_numerador + agrupamento_pessoas[c]['Idade'] 

media = soma_numerador/soma_pessoas
print(f'Foram cadastradas {soma_pessoas} pessoas.')
print(f'A média de idade do grupo é de {media:.1f}.')

print('As mulheres cadastradas foram:')
for c in range(0, len(agrupamento_pessoas)):
    if agrupamento_pessoas[c]['Sexo'] == 'F':
        print(f'{agrupamento_pessoas[c]["Nome"]}...', end='')

print('\nPessoas com a idade maior que a média: ')
for c in range(0,len(agrupamento_pessoas)):
    if agrupamento_pessoas[c]['Idade'] > media:
        print(f'Nome = {agrupamento_pessoas[c]["Nome"]}; Sexo = {agrupamento_pessoas[c]["Sexo"]}; Idade = {agrupamento_pessoas[c]["Idade"]}')
print(agrupamento_pessoas)







