#Desafio 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#  - Á vista dinheiro/cheque: 10% de desconto.
#  - Á vista no cartão: 5% de desconto.
#  - Em até 2x no cartão: preço normal.
#  - 3x ou mais no cartão: 20% de juros.

gomes = 'LOJAS GOMES'
print(f'{gomes:-^30}')
valor = float(input('Qual o preço do produto? '))
metd = 'MÉTODO DE PAGAMENTO'
print(f'{metd:-^30}')

print('''[ 1 ] - Á vista no DINHEIRO/CHEQUE: 
[ 2 ] - Á vista no CARTÃO:
[ 3 ] - Em até 2x no CARTÃO:
[ 4 ] - 3x ou mais no CARTÃO:''')
escolha = int(input('Escolha um método de pagamento: '))

if escolha == 1:
    print(f'Sua compra de R${valor:.2f} sairá por \033[37;42mR${(valor - valor*0.10):.2f}\033[m')
elif escolha == 2:
    print(f'Sua compra de R${valor:.2f} sairá por \033[37;42mR${(valor - valor*0.05):.2f}\033[m')
elif escolha == 3:
     parcela = int(input('Quantas Parcelas? '))
     if 0<parcela<=2:
        print(f'O valor da sua compra será o mesmo, \033[37;42mR$R${valor:.2f}\033[m SEM JUROS.')
     else:
        print(f'OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')
elif escolha == 4:
    parcela = int(input('Quantas Parcelas? '))
    print(f'''A sua compra será parcelada em {parcela:.0f}x de R${((valor+valor*0.2)/parcela):.2f} no cartão, COM JUROS. 
    Sua compra de R${valor:.2f} vai custar \033[37;41mR${(valor+valor*0.2):.2f}\033[m no final. ''')
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')