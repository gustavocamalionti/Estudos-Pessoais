#Desafio 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

text1 = 'LISTAGEM DE PREÇOS: MODO 1'
print('-'*31)
print(f'{text1:^31}')
print('-'*31)

prodprice = ('Impressora', 149.99, 'Moletom', 80.00, 'Caderno', 10.00, 'Estojo', 5.99, 'Livro', 25.99, 'Mochila', 129.99)

for c in range(0, len(prodprice)):
    if c%2==0:
        print(f'{prodprice[c]:.<21}', end='')
    else:
        print(f'R$ {prodprice[c]:>7.2f}')

text2 = 'LISTAGEM DE PREÇOS: MODO 2'
print('-'*31)
print(f'{text2:^31}')
print('-'*31)

#SEGUNDA RESOLUÇÃO
for c in range(0, len(prodprice), 2):
    print(f'{prodprice[c]:.<21}R$ {prodprice[c+1]:>7.2f}')