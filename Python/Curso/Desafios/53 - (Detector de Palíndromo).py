#Desafio 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 

#Ex: Ana 
#ex: Apos a sopa 
#Ex: A Sacada da Casa 
#ex: O lobo ama o bolo 
#ex: anotaram a data da maratona

frase = str(input('Digite uma frase ou nome qualquer: ')).strip().upper()
palavra = frase.split()
junto =''.join(palavra)
inverso = ''

for c in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[c]
print(inverso)
print(f'O inverso de {junto} é {inverso}. ')
if inverso == junto:
    print(f'{junto} É uma palavra/frase/nome Políndroma. ')
else:
    print(f'{junto} Não é uma palavra/frase/nome Políndroma.')