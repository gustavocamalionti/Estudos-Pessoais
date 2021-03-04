#Desafio 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p1 = float(input('Qual o preço do produto, sem desconto? '))
d = p1 - (p1*0.05)
print(f'Sem desconto ele vale R${p1:.2f} reais. Na promoção com 5% de desconto, ele vai custar R${d:.2f} reais. ')