nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
     print('Que nome bonito.')
elif nome == 'Maria' or nome =='Paulo' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Julia Janaina Patrícia Joanna':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}! ')

#DIFERENÇA ENTRE if e else
#mostre se um número é 