#Desafio 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p1 = float(input('Qual o preço do produto, sem desconto? '))
d = p1*0.05
vr = p1-d
print(f'Sem desconto ele vale R${p1:.2f} reais. Se aplicarmos 0.05x de desconto, teremos R${vr} reais. ')