
#Condição Simples (sem else)
cs = 'CONDIÇÃO SIMPLES'
print(f'{cs:-^40}')

nome = str(input('Qual seu primeiro nome? '))
if nome == 'Gustavo':
    print('Que nome bonito.')
print(f'Bom dia {nome}!')

#Condição Composta (Com else)
cd = 'CONDIÇÃO COMPOSTA'
print(f'{cd:-^40}')

nome = str(input('Qual o seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito. ')
else:
    print('Que nome Feio! hahaah brincadeira.')
print(f'Bom dia {nome}! ')

#Cálculo de Média: CONDICIONAL
med = 'CONDICIONAL:CÁLCULO DE MÉDIA'
print(f'{med:-^40}')

n1 = float(input('Digite sua nota na primeira prova: '))
n2 = float(input('Digite sua nota na segunda prova: '))
m = (n1+n2)/2 

print(f'Sua média com a P1 e P2 foi de: {m:.1f} ')
if m >= 6.0:
    print(f' Parabéns, você foi APROVADO! ')
else:
    print(f'Estude mais, você foi REPROVADO! ')

g = 'Gustavo'
