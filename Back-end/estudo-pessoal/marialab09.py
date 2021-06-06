#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Magic: Trocando Cartas
# Nome: 
# RA: 
#####################################################


banco_cartas = list()
desejadas_cartas = list()
trocas_processamento = list()
contem_desejada_perde = bool
contem_desejada_ganha = bool
validacao_desejada = bool
validacao = bool
contem_desejada = bool
# Leitura das cartas para troca
num_cartas = int(input())
for c in range(0, num_cartas):
    banco_cartas.append(input().split())

# Leitura das cartas desejadas
num_desejadas = int(input())
for c in range (0, num_desejadas):
    desejadas_cartas.append(input().split())


# Processamento das trocas
processamento = ''
while processamento != '---':
    processamento = input()
    trocas_processamento.append(processamento.split())

trocas_processamento.pop()


# Processamento se as cartas desejadas foram obtidas

for a in range(0, len(trocas_processamento)):
    for b in range(0, len(banco_cartas)):
        #INTELIGENCIA - ENCONTRANDO A CARTA PERDIDA 
        for g in range(0, len(banco_cartas)):
            contem_perdida = False
            if banco_cartas[g][0] == trocas_processamento[a][1]:
                contem_perdida = True
                break

            else:
                contem_perdida = False
        
        for g in range(0, len(banco_cartas)):
            contem_ganhada = False
            if banco_cartas[g][0] == trocas_processamento[a][0]:
                contem_ganhada = True
                break

            else:
                contem_ganhada = False

        for i in range(0, len(desejadas_cartas)):    
            contem_desejada_ganha = False
            if trocas_processamento[a][0] == desejadas_cartas[i][0] and banco_cartas[g][0] == trocas_processamento[a][0]:
                contem_desejada_ganha = True
                break

            else:
                contem_desejada_ganha = False 

        for i in range(0, len(desejadas_cartas)):
            contem_desejada_perde = False
            if trocas_processamento[a][1] == desejadas_cartas[i][0] and banco_cartas[b][0] == trocas_processamento[a][1]:
                contem_desejada_perde = True
                break

            else:
                contem_desejada_perde = False 

    print(f'----------- TROCA: \033[31;40m{trocas_processamento[a]}\033[m || BANCO: \033[32;40m{banco_cartas}\033[m ----------- \n Contem_ganhada: {contem_ganhada} \n Contem_perdida: {contem_perdida} \n Contem_desejada_perde: {contem_desejada_perde} \n Contem_desejada_ganha: {contem_desejada_ganha}')
   
        