#Desafio 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 

#Ex: Ana 
#ex: Apos a sopa 
#Ex: A Sacada da Casa 
#ex: O lobo ama o bolo 
#ex: anotaram a data da maratona

frase = str(input('Digite uma frase ou nome qualquer: ')).strip().upper()
lista = frase.split()
junto =''.join(lista)
inverso = ''


for c in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[c]
print(inverso)
print(f' O inverso de {junto} é {inverso}.')
if inverso == junto:
    print(f' É uma palavra/frase Políndroma.')
else:
    print(f'Não é Políndroma')