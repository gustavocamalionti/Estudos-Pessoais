 
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 21} #pessoas= dict()
print(pessoas)

print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print()

print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

print()

for k in pessoas.keys():
    print(k)

print()

for v in pessoas.values():
    print(v)

print()

for k, v in pessoas.items():
    print(f'{k} = {v}')

print()
#mudando o dicionário
pessoas['nome'] = 'Leandro'
del pessoas['sexo'] #apagando keys 'sexo'
print(pessoas)
pessoas['peso'] = 73.3
print(pessoas)

for k, v in pessoas.items():
    print(f'{k} = {v}')

#criando dicionário dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print()

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

print()

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #O fatiamento tradicional não funciona para dicionários, usamos .copy()
print(brasil)

print()

for e in brasil:
    print(e)

print('-'*25)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

print('-'*25)
for e in brasil:
    for v in e.values():
        print(f'{v} ', end='')
    print()
