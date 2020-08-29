import colorama #O WINDOWS N SUPORTA A SEQUÊNCIA (ANSI).
colorama.init()

#EXEMPLOS:
print('\033[33;41mHello World!\033[m ')
print('\033[31;43mHello World!\033[m ')
print('\033[30;47mHello World!\033[m ')
print('\033[37;40mHello World!\033[m ')

print('-=-'*20)
a = 3
b = 5
print(f'O valor digitado é \033[31m{a}\033[m e \033[32m{b}\033[m!!!')
nome = 'Gustavo'
print(f'Muito prazer em te conhecer, \033[30;47m{nome}!!!\033[m ')
print('-=-'*20)

#CASO 1: DICIONÁRIO
nome = 'Gustavo'
cores = { "limpa":"\033[m",
          "vermelha":"\033[31m",
          "verde":"\033[32m",
          "pretoebranco":"\033[30;47m"}
print(f'Muito prazer em te conhecer, {cores["vermelha"]}{nome}{cores["limpa"]}. ')
print(f'Muito prazer em te conhecer, {cores["pretoebranco"]}{nome}{cores["limpa"]}')

#CASOS PECULIARES
      #FOREGROUND(LETRA)/BACKGROUND(FUNDO):
'\033[30;40m'      # black/black
'\033[31;40m'      # red/red
'\033[32;40m'     # green/green
'\033[33;40m'     # yellow/yellow
'\033[34;44m'    # blue/blue
'\033[35;45m'     # magenta/magenta
'\033[36;46m'      # cyan/cyan
'\033[37;47m'      # white/white
'\033[39;48m'      # reset/reset
     
 # CORES E BRILHOS
'\033[1m'       # bright
'\033[2m'       # dim (looks same as normal brightness)
'\033[22m'      # normal brightness