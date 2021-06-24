#Desafio 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

larg = float(input('Qual a largura da parede? em metros. '))
alt = float(input('Qual a altura da parede? em metros. '))
area = larg*alt
print(f'Então a área total da parede, tendo em vista que a largura é de {larg} e a altura {alt}, vale {area}m². Além disso, se gastassemos 1 litro de tinta para cada 2m², deveriamos comprar aproximadamente {area/2:.1f}L de tinta. ')