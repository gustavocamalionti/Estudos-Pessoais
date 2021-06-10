#Desafio 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
# A) Quantas pessoas tem mais de 18 anos. 
# B) Quantos homens foram cadastrados. 
# C) Quantas mulheres tem menos de 20 anos.  

conth = 0
pessoas18 = 0
contm = 0
c = 0
while True:
    print('-'*10,'CADASTRO','-'*10)
    nome = str(input('Qual seu nome? ')).upper().strip()
    idade = int(input('E sua idade? '))
    if idade>=18:
        pessoas18 = pessoas18 + 1

    sexo = str(input('Para finalizar, qual seu sexo? [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        conth = conth + 1
    if sexo == 'F' and idade<20:
            contm = contm + 1

    while sexo not in 'MF':
        sexo = str(input('CARÁCTER INVÁLIDO!!! qual seu sexo [M/F]? ')).strip().upper()[0]
        if sexo == 'M':
            conth = conth + 1
        if sexo == 'F' and idade<20:
            contm = contm + 1
    

    print('-=-'*15)
    print(f'CADASTRO EFETUADO COM SUCESSO!!!')
    print('-=-'*15)

    opcao = str(input('Deseja continuar com novos cadastros [\033[32mS\033[m/\033[31mN\033[m]? ')).strip().upper()[0]

    while opcao not in 'SN':
        opcao = str(input('Por favor, escolha entre [\033[32mS\033[m/\033[31mN\033[m]: ')).upper().strip()[0]
    if opcao == 'N':
        break

print(f'Total de pessoas maiores de 18 anos: {pessoas18}')
print(f'Quantidade de homens cadastrados: {conth}')
print(f'Total de mulheres menores de 20 anos cadastradas: {contm}')
