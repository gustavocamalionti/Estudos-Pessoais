#Desafio 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def área(a, b):
    area = a*b
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} vale {area:.1f} m²')
    

#Programa Principal
largura = float(input('Digite a Largura (m): '))
comprimento = float(input('Digite o comprimento (m): '))

área(largura, comprimento)
