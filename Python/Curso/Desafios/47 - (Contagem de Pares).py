#Desafio 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('Números Pares entre 1 e 50: ')
print('=-='*20)

for c in range(1, 51, 2):
    print(c+1, end=' ')
print(' FIM')

for c in range(1,51) :
    if c%2==0:
        print(c, end=' ')
print(' FIM')