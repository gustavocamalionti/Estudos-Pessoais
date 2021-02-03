#Desafio 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def área(a, b):
    area = a*b
    print(f'A área vale {area} m².')
    

#Programa Principal
largura = float(input('Digite a Largura: '))
comprimento = float(input('Digite o comprimento: '))

área(largura, comprimento)
