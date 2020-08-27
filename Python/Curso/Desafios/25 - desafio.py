#Desafio 024: Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

name = str(input('Digite seu nome completo: ')).upper()
lista = name.split()
print(f'Seu nome possui Silva. {name}, essa afirmação é verdadeira? {"SILVA" in lista}.')