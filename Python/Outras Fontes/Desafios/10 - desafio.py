#Desafio 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Considere US$1,00=3,27

money = float(input('Quantos reais você tem na carteira? '))
d = money/3.27
print(f'Com R${money:.3f} reais você conseguiria comprar, tendo em vista que o dolar vale R$3.27 reais, US${d:.3f}. ')
#print(f'Com R${money:3f} reais voce conseguiria comprar, tendo em vista que o dolar vale R$3.27 reais, US${money/3.27:.3f} ')