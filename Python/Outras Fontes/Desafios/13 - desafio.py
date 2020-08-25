#Desafio 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sl = float(input('Qual o seu salário atual? '))
al = sl*0.15
vt = sl + al
print(f'Parabéns! Você acaba de receber um aumento de 0.15x no salário! apartir de hoje receberá um montante de R${vt:.2f} reais.')