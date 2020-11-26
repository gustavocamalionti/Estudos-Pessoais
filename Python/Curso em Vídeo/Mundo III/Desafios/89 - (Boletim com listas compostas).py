#Desafio 89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

#RESOLUÇÃO PESSOAL
dados = []
lista_notas_alunos = []

while True:
    nome = str(input('Digite um nome: ')).strip().upper()
    nota_1 = float(input('Nota da P1: '))
    nota_2 = float(input('Nota da P2: '))
    lista_notas_alunos.append([nome, nota_1, nota_2])
    dados.clear()

    continuar_questao = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar_questao not in 'SN':
        continuar_questao = str(input('Caracter inválido, tente novamente. Quer continuar? [S/N]')).strip().upper()
    if continuar_questao == 'N':
        break

titulo = 'QUADRO GERAL DE NOTAS'
print('-'*30)
print(f'{titulo:^30}')
print('-'*30)

print(f'{"N":<2}{"NOME":<25}{"MÉDIA":<3}') 

for c in range(0, len(lista_notas_alunos)):
    print(f'{c:<2}{lista_notas_alunos[c][0]:<25}{((lista_notas_alunos[c][1]+lista_notas_alunos[c][2])/2):<3.1f}')

while True:
    mostrar_notas = int(input('Mostrar notas de qual aluno? (999 para interromper) '))
    for c in range(0, len(lista_notas_alunos)):
        if mostrar_notas == c:
            print(f'As notas de {lista_notas_alunos[c][0]} na P1 e P2 foram, respectivamente: ', end='')
            if lista_notas_alunos[c][1]>=5:
                print(f'\033[32m{lista_notas_alunos[c][1]:.1f}\033[m ', end='e ') 
            else:
                print(f'\033[31m{lista_notas_alunos[c][1]:.1f}\033[m ', end='e ')
            
            if lista_notas_alunos[c][2]>=5:
                print(f'\033[32m{lista_notas_alunos[c][2]:.1f}\033[m.')
            else:
                print(f'\033[31m{lista_notas_alunos[c][2]:.1f}\033[m.')
    if mostrar_notas == 999:
        print('Fechando programa, obrigado!')
        break

