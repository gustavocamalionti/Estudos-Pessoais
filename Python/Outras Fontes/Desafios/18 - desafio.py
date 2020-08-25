#Desafio 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians

a = float(input('Digite um ângulo(em graus) e receba os valores em sen, cos e tg desse ângulo. '))
ar = radians(a)
print(f'sen({a:.0f}°) = {sin(ar):.2f} ')
print(f'cos({a:.0f}°) = {cos(ar):.2f} ')
print(f'tg({a:.0f}°) = {tan(ar):.2f} ')
