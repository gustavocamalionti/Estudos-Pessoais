#Desafio 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#MODO 1:
m1 = 'MODO 1'
print(f'{m1:-^20}')
a = float(input('1° número: '))
b = float(input('2° número: '))
c = float(input('3° número: '))

#CASOS NORMAIS:
if  a<b and a<c:
    print(f'menor = {a:.2f}. ')
if b<a and b<c:
    print(f'menor = {b:.2f}. ')
if c<a and c<b:
    print(f'menor = {c:.2f}. ')
if  a>b and a>c:
    print(f'Maior = {a:.2f}. ')
if b>a and b>c:
    print(f'Maior = {b:.2f}. ')
if c>a and c>b:
    print(f'Maior = {c:.2f}. ')

#CASOS PECULIARES:
if a==b and b==c:
    print(f'Todos os números são iguais.')
if a==b and c<a:
    print(f'Dois números são iguais e sabemos que {c:.2f} é o menor e {a:.2f} é o maior. ')
if a==c and b<a:
    print(f'Dois números são iguais e sabemos que {b:.2f} é o menor e {a:.2f} é o maior. ')
if b==c and a<b:
    print(f'Dois números são iguais e sabemos que {a:.2f} é o menor e {b:.2f} é o maior. ')
if a==b and c>a:
    print(f'Dois números são iguais e sabemos que {c:.2f} é o maior e {a:.2f} é o menor. ')
if a==c and b>a:
    print(f'Dois números são iguais e sabemos que {b:.2f} é o maior e {a:.2f} é o menor. ')
if b==c and a>b:
    print(f'Dois números são iguais e sabemos que {a:.2f} é o maior e {b:.2f} é o menor. ')


#MODO 2 = desconsiderando os casos peculiares
m1 = 'MODO 2'
print(f'{m1:-^20}')
a = float(input('1° número: '))
b = float(input('2° número: '))
c = float(input('3° número: '))

l = [a, b, c]
print(f'MENOR{min(l)}')
print(f'MAIOR{max(l)}')