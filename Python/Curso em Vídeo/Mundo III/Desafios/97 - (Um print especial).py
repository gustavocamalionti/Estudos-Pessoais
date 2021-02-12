#Desafio 97: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 
# Ex:escreva('Olá, mundo!') 
# 
# Saída:    ------- 
#         Olá, Mundo
#           -------

def escreva(msg):
    print(f'{"-"*30}')
    print(f'{msg:^30}')
    print(f'{"-"*30}')
#Programa Principal
msg = str(input(f'Escreva qualquer coisa: '))

escreva(msg)
escreva('Aluno: Gustavo')