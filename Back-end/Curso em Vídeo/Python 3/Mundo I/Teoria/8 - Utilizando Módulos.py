#Módulo Math Geral
import math #faça, import [CTRL+ESPAÇO]
n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print(f'A raiz de {n} é {raiz:.3f}. ')

#Módulo Math Específico
from math import sqrt
n = int(input('Digite um número: '))
print(f'A raiz de {n} é {sqrt(n):.3f}. ')

#Módulo random
import random
num1 = random.random() 
print('Computador, me dê um número aleatório entre 0 e 1:',num1)

num2 = random.randint(1,100)
print('Computador, agora eu quero um número inteiro:',num2)
#Importando uma biblioteca da comunidade: Para importar uma biblioteca do pypi, necessita usar no terminal o comando(pip install "E o nome do pacote, sem as aspas")

import emoji
print(emoji.emojize('Python é legal :thumbsup:', use_aliases = True))