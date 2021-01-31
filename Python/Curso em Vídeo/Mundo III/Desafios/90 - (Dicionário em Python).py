#Desafio 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

<<<<<<< Updated upstream
#RESOLUÇÃO PESSOAL
aluno = {}
aluno['nome'] = str(input('Nome: ')).upper()
aluno['média'] = float(input(f'A média de {aluno["nome"]} é: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'

elif 5<= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'

else:
    aluno['situação'] = 'Reprovado'

for k,v in aluno.items():
    print(f'{k} é igual a {v}')
=======
dicionario = ['nome':'', 'media':'', 'situacao':'',]
if 5<=dicionario['media']<7:
    print()

    



>>>>>>> Stashed changes
