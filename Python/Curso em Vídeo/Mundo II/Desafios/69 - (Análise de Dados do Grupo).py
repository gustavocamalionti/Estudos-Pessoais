#Desafio 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
# A) Quantas pessoas tem mais de 18 anos. 
# B) Quantos homens foram cadastrados. 
# C) Quantas mulheres tem menos de 20 anos.  

c = 0
while True:
    print('-'*10,'CADASTRO','-'*10)
    nome = str(input('Qual seu nome? ')).upper().strip()
    idade = int(input('E sua idade? '))
    sexo = str(input('Para finalizar, qual seu sexo? [M/F] ')).strip().upper()[0]
    
    while sexo not in 'MF':
        sexo = str(input('CARÁCTER INVÁLIDO!!! qual seu sexo [M/F]? ')).strip().upper()[0]
    print('-=-'*25)
    print(f'CADASTRO EFETUADO COM SUCESSO!!! \n{nome} \n{idade} \n{sexo}. ')
    print('-=-'*25)
    opcao = str(input('Deseja continuar com novos cadastros [\033[32mS\033[m/\033[31mN\033[m]? ')).upper().strip()[0]
    if opcao == 'N':
        break
    while opcao not in 'SN':
        opcao = str(input('Por favor, escolha entre [\033[32mS\033[m/\033[31mN\033[m]: ')).upper().strip()[0]
    c = c + 1
print('Obrigado por usar o programa.')
