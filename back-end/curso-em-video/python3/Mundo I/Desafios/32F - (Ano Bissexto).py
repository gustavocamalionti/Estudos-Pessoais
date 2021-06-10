#Desafio 032: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

import datetime
ano = int(input('Em que ano estamos? Coloque 0 para analisar o ano atual se preferir. '))
if ano == 0: 
    ano = datetime.date.today().year
if ano%4==0 and ano%100 !=0 or ano%400==0: #!= é diferente
    print(f'{ano} é BISSEXTO.')
else:
    print(f'{ano} não é BISSEXTO.')