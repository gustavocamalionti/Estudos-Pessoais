#Desafio 017: Faça um program que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import pow, sqrt

ca = float(input('Digite um valor para o cateto adjacente: '))
co = float(input('Digite um valor para o cateto oposto: '))
h = sqrt(pow((ca), 2)+pow((co), 2))

print(f'tendo em vista que o CA = {ca:.7f} e o CO = {co:.7f}. Então o valor da hipotenusa vale {h:.7f}. ')
