#Desafio 063: Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci. Ex: 0 1 1 2 3 5 8

print('-'*30)
print('Sequência de Fibonnaci')
print('-'*30)
n = 0
while n<2:
    n = int(input('Quer mostrar quantos termos da sequência? '))
    if n<2:
        print('Por favor, digite um número maior ou igual a 2')

c = 1
t1 = 0
t2 = 1

while c<=n:
    print(t1, end = ' ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c = c + 1
print('FIM')

#REVISAR
print('\n','-'*30)
print('Sequência de Fibonnaci: outra resolução')
print('-'*30)
n = int(input('Quer mostrar quantos termos da sequência? '))

Nant=1
fibonacci=0

while n!=0:
    print(f'{fibonacci}')
    fibonacci = fibonacci + Nant
    Nant = fibonacci - Nant
    n = n - 1
print('Fim')

