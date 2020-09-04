for c in range(0,6):
    print('Hello, World!')
print('FIM')

print('-'*30)

for c in range(0,6):
    print(c)
    print('FIM')

print('-'*30)

for c in range(6, 0, -1):
    print(c)
print('FIM')

print('-'*30)

for c in range(0, 7, 2):
    print(c)
print('FIM')

print('-'*30)

n = int(input('Digite um Número: '))
for c in range(0, n+1):
    print(c)

print('-'*30)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passos: '))
for c in range(i,f+1, p):
    print(c)

print('-'*30)

s = 0
for c in range(0,3):
    n = int(input('Digite um Valor: '))
    s += n #s = s + n 
print(f'O somatório de todos os valores vale {s}.')


print('-'*30)