#Desafio 037: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
#-1 para binário. 
#-2 para octal.
#-3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
print('-=-'*40)
print('''[1] - Converter para BINÁRIO. 
[2] - Converter para OCTAL. 
[3] - Converter para HEXADECIMAL.''')

print('-=-'*40)
escolha = int(input('Escolha uma opção: '))
if escolha==1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]} ')
elif escolha==2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]} ')
elif escolha==3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]} ')
else:
    print(f'{escolha} é uma opção INVÁLIDA! Tente novamente.')

