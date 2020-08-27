 #Desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
 #O nome com todas as letras maiúsculas. 
 #O nome com todas minúsculas. 
 #Quantas letras ao todo (sem considerar espaços). 
 #Quantas letras tem o primeiro nome.


#MODO 1: Feito sozinho, sem ajuda de gabarito.
name = str(input('Digite o seu nome: '))
print('Analisando...')

letras = len(name)
espacos = name.count(' ')
lista = name.split()

print(f'seu nome em maíusculo: {name.upper()}. ')
print(f'Seu nome em minúsculo: {name.lower()}. ')
print(f'Há {letras - espacos} letras em seu nome. ')
print(f'Seu nome inicial é {lista[0]} e ele possui {len(lista[0])} letras.')

#Modo 2: Resolução do Professor.
