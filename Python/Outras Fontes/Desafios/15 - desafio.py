#Desafio 015: escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

from math import ceil
n1 = float(input('Quantos dias você ficou com o carro? '))
n2 = float(input(f'Ok. já que você ficou {ceil(n1)} dias com ele, andou quantos km? '))
v = n1*60 + n2*0.15
print(f'Legal. Então você precisará pagar R${v:.2f} pelo aluguel. ')