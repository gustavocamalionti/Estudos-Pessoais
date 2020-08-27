#Desafio 024: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
# Ex: Ana Maria de Souza 
# primeiro = Ana 
# último = Souza



#MODO 1: RESOLUÇÃO PESSOAL V1
name = str(input('Digite seu nome: '))
list = name.split()
print(f'Primeiro:{list[0]}. ')
print(f'Último:{list[-1]}.')

#MODO 2: RESOLUÇÃO PESSOAL V2
name2 = str(input('Digite seu nome: '))
print(f'Primeiro nome: {name2.split()[0]}. ')
print(f'Último nome: {name2.split()[-1]}. ') #Usa-se -1 para inverter a ordem(O primeiro da direita para a esquerda -1).

#MODO 3: RESOLUÇÃO DO PROFESSOR
name3 = str(input('Digite o seu nome: '))
lista = name3.split()
print(f'Primeiro:{lista[0]}. ')
print(f'Último: {lista[len(lista)-1]}. ')

