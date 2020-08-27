 #Desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
 #O nome com todas as letras maiúsculas. 
 #O nome com todas minúsculas. 
 #Quantas letras ao todo (sem considerar espaços). 
 #Quantas letras tem o primeiro nome.


#MODO 1: Feito sozinho, sem ajuda de gabarito.
name = str(input('Digite o seu nome: '))

letras = len(name)
espacos = name.count(' ')
lista = name.split()

print('Analisando...')
print(f'seu nome em maiúsculo: {name.upper()}. ')
print(f'Seu nome em minúsculo: {name.lower()}. ')
print(f'Há {letras - espacos} letras em seu nome. ')
print(f'Seu nome inicial é {lista[0]} e ele possui {len(lista[0])} letras.')

#Modo 2: Resolução do Professor.(esse modo só funciona bem se a pessoa digitasse o nome completo dela, caso fosse apenas o primeiro nome, daria erro! A minha resolução considera todos os casos.)
name = str(input('Digite seu nome aqui: ')).strip()

print('Analisando...')
print(f'Seu nome em maiúsculo é {name.upper()}. ')
print(f'Seu nome em minúsculo é {name.lower()}. ')
print('Há {} letras em seu nome. '.format(len(name) - name.count(' ')))
print('Seu primeiro nome tem {} letras em seu nome.'.format(name.find(' ')))


