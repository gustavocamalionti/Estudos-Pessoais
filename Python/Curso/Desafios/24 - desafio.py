#Desafio 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".




#MODO 1: Resolução pessoal - Cobre todas as possibilidades.
city = str(input('Nos informe a cidade onde você nasceu, por gentileza. ')).upper() #O split já exclui os espaços iniciais e finais, logo, não precisa usar .strip
lista = city.split()
print(f'O nome dela começa com Santo? {lista[0] == "SANTO"}.')

#MODO 2:Professor - Cidados do tipo: santorini dá valor 'True" mesmo sendo falso.
cid = str(input('Em que cidade você nasceu? '))
print(f'a cidade começa com Santo? {cid[:5].upper() == "SANTO"}')
