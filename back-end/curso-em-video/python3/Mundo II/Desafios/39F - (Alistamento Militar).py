#Desafio 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: -Se ele ainda vai se alistar ao serviço militar.
#  - Se é a hora de se alistar.
#  - Se já passou do tempo do alistamento. 
# - Seu programa também devera mostrar o tempo que falta ou que passou do prazo.

import datetime
anonascimento = int(input('Ano de nascimento: '))
anoatual = datetime.date.today().year
idade = anoatual - anonascimento

print(f'Quem nasceu em {anonascimento} possui {idade} anos em {anoatual}.')
if idade==18:
    print(f'Está na hora de se alistar. ')
elif idade<18:
    print(f'Ainda faltam {(18 - idade)} anos para seu alistamento. Ele acontecerá em {(18-idade) + anoatual}.')
else: 
    print(f'Você já deveria ter se alistado a {idade - 18} anos. O alistamento aconteceu em {anoatual - (idade - 18)}. ')



