#Desafio 029: Escreva um programa que leia a velocidade de um carro. #Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7.00 por cada km acima do limite.

v = float(input('Qual a velocidade do seu carro(km/h)? '))

mult = 7*(v-80)
if v>80:
    print(f'Velocidade muito alta, você foi multado em {mult:.2f} reais! Da proxima vez, fique no limite.')
else:
    print('Você está assumindo uma postura defensiva, continue assim! ')