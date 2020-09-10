#Desafio 058: Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random 
numeromaquina = random.randint(1,10)
print('-'*50)
print('Pensei em um número entre 1 e 10... Tente adivinhar!')
print('-'*50)

somaerro = 0
numerousuario = ''
opcaoinvalida = 0

numerousuario = int(input('Qual você escolhe? '))
somaerro = somaerro + 1  
while not numerousuario == numeromaquina:
    if numerousuario>numeromaquina and (1<=numerousuario<=10):
        numerousuario = int(input('Menos... Escolha outro valor: '))
        somaerro = somaerro + 1
    if numerousuario<numeromaquina and (1<=numerousuario<=10):
        numerousuario = int(input('Mais... Escolha outro valor: '))
        somaerro = somaerro + 1
    if numerousuario>10 or numerousuario<1:
        opcaoinvalida = opcaoinvalida + 1
        numerousuario = int(input('\033[31mOPÇÃO INVÁLIDA!\033[m Tente novamente: '))
        somaerro = somaerro + 1

print(f'Parabéns, você me \033[32mVENCEU!\033[m foi necessário {somaerro - opcaoinvalida} tentativas até encontrar [{numeromaquina}], o número sorteado. ')