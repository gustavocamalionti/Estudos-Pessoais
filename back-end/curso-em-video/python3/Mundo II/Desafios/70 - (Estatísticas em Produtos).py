#Desafio 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: 
# A) Qual é o total de gasto na compra. 
# B) Quantos produtos custam mais de R$1000. 
# C) Qual é o nome do produto mais barato.



loja = 'LOJA SUPER BARATÃO'
print('-'*30)
print(f'{loja:^30}')
print('-'*30)

soma = menorp = maiorp = menorn = maiorn = cont = c = 0

while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('PREÇO: R$ '))
    c = c + 1
    if c==1:
        menorp = preco
        menorn = produto
        maiorp = preco
        maiorn = produto

    else:
        if preco<menorp:
            menorp = preco
            menorn = produto

        if preco>maiorp:
            maiorp = preco
            maiorn = produto

    if preco>1000:
        cont = cont + 1
    
    soma = soma + preco

    opcao = str(input('Quer continuar? [\033[32mS\033[m/\033[31mN\033[m] ')).strip().upper()
    while opcao not in 'SN':
        opcao = str(input('DIGITE NOVAMENTE. [\033[32mS\033[m/\033[31mN\033[m]? ')).strip().upper()
    if opcao == 'N':
        break
    
print(f'Valor da Compra Total: R${soma}')
print(f'temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menorn} que custa R${menorp}')