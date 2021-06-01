test = list()
test.append('Gustavo')
test.append('40')

galera = list()
galera.append(test[:])
test[0] = 'Maria'
test[1] = '22'
galera.append(test[:])
print(galera)

grupos = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(grupos)
print(grupos[0])
print(grupos[0][0])
print(grupos[2][1])

print('-=-'*20)

for p in grupos:
    print(p) 

print('-=-'*20)

for p in grupos:
    print(p[0]) #apenas os nomes

print('-=-'*20)

for p in grupos:
    print(p[1]) #apenas as idades

print('-=-'*20)

for p in grupos:
    print(f'{p[0]} tem {p[1]} anos de idade') #apenas as idades

print('-=-'*20)


pessoas = list()
dado = list()
maior_idade=menor_idade=0

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()
print(pessoas)

for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        maior_idade = maior_idade + 1
    else:
        print(f'{p[0]} é menor de idade. ')
        menor_idade = menor_idade = 1
print(f'Temos {maior_idade} maiores de idades e {menor_idade} menores de idade. ')