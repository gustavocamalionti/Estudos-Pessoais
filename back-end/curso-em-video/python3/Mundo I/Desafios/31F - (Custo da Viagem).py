#Desafio 031: Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

dist = float(input('Qual a distância de sua viagem? '))
pr = 0.50*dist
prm = 0.45*dist

if dist<=200:
    print(f'Você pagará: {pr:.2f}. ') 
else:
    print(f'Como você ultrapassou 200km com o carro, pagará um total de {prm:.2f}. ')