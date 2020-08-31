#Desafio 042: Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#  - Equilátero: todos os lados iguais.
#  - Isósceles: dois lados iguais.
#  - Escaleno: todos os lados diferentes.

#MODO 1: SOZINHO
p = 'SOZINHO'
print(f'{p:-^50}')
a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))

if c<(a+b) and b<(a+c) and a<(b+c) and (a==b==c):
    print('O triângulo existe e ele é \033[37;45mEquilátero!\033[m Todos os lados são iguais.')
elif c<(a+b) and b<(a+c) and a<(b+c) and (a==b or a==c or c==a):
    print('O triângulo existe e ele é \033[37;45mIsósceles!\033[m Possui 2 lados iguais.') 
elif c<(a+b) and b<(a+c) and a<(b+c) and (a!=b!=c):
    print('O triângulo existe e ele é \033[37;45mEscaleno!\033[m Todos os lados são diferentes.')
else:
    print('O triângulo não existe.')

#MODO 2: PROFESSOR
p = 'PROFESSOR'
print(f'{p:-^50}')
a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))

if c<(a+b) and b<(a+c) and a<(b+c):
    print('O triângulo existe: ', end='')
    if a==b==c:
        print('Ele é \033[37;45mEquilátero!\033[m. Todos os lados são iguais.')
    elif a!=b!=c!=a:
        print('Ele é \033[37;45mEscaleno!\033[m. Todos os lados são diferentes. ')
    else:
        print('Ele é \033[37;45mIsósceles!\033[m. Possui 2 lados iguais. ')
else:
    print('O triângulo não existe.')

#MODO 3:TESTE
p = 'TESTE'
print(f'{p:-^50}')
a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))
 
if c<(a+b) and b<(a+c) and a<(b+c): #CONDIÇÕES ANINHADAS
    if a==b==c:
        print('O triangulo existe e ele é \033[37;45mEquilátero!\033[m. Todos os lados são iguais.')
    elif a!=b!=c!=a:
        print('O triangulo existe e ele é \033[37;45mEscaleno!\033[m. Todos os lados são diferentes. ')
    else:
        print('O triangulo existe e ele é \033[37;45mIsósceles!\033[m. Possui 2 lados iguais. ')
else:
    print('O triângulo não existe.')