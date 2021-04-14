#Desafio 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sl = float(input('Qual o seu salário atual? '))
al = sl + (sl*0.15)
print(f'Parabéns! Você acaba de receber um aumento de 15% no salário! apartir de hoje receberá um montante de R${al:.2f} reais.')