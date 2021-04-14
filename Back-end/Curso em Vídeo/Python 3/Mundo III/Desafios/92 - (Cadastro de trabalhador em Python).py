#Desafio 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

#RESOLUÇÃO PESSOAL
from datetime import datetime

empregado = {'Nome': str(input('Digite seu nome: ')),
             'Idade':datetime.now().year - int(input('Ano de nascimento: ')),
             'Numero da carteira': int(input('Carteira de Trabalho(0 não tem): '))}

if empregado['Numero da carteira'] != 0: 
    empregado['Ano de contratação'] = int(input('Ano de contratação: '))
    empregado['Salário'] = float(input('Qual o seu salário? '))
    empregado['Aposentadoria'] =  empregado['Idade'] + ((empregado['Ano de contratação'] + 35) - datetime.now().year)
    for k,v in empregado.items():
        print(f'- {k} tem o valor {v}. ')

else:
    for k,v in empregado.items():
        print(f'- {k} tem o valor {v}. ')




