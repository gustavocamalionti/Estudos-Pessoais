#PROFESSOR
import random
maquina = random.randint(1,10)
print('-'*50)
print('Pensei em um número entre 1 e 10... Tente adivinhar!')
print('-'*50)
acertou = False
palpite = 0 

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite = palpite + 1
    if jogador==maquina:
        acertou = True
    else:
        if jogador>maquina:
            print('Menos... Tente novamente: ')
        elif jogador<maquina:
            print('Mais... Tente novamente: ')
print(f'Acertou!!! foi necessário {palpite} palpites até encontrar o valor sorteado [{maquina}].')