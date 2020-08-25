#Módulo Geral
import math
n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print(f'A raiz de {n} é {raiz:.3f}. ')

#Módulo Específico
from math import sqrt
n = int(input('Digite um número: '))
print(f'A raiz de {n} é {sqrt(n):.3f}. ')

#Importando uma biblioteca da comunidade: Para importar uma biblioteca do pypi, necessita usar no terminal o comando(pip install "E o nome do pacote, sem as aspas")

import emoji
print(emoji.emojize('Python é legal :thumbsup:', use_aliases = True))