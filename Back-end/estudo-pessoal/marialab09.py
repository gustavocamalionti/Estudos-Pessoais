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

#INTELIGENCIA 
    #PERDIDA
    for g in range(0, len(banco_cartas)):
        contem_perdida = False
        if banco_cartas[g][0] == trocas_processamento[a][1]:
            contem_perdida = True
            break

        else:
            contem_perdida = False
    
    #GANHADA
    for g in range(0, len(banco_cartas)):
        contem_ganhada = False
        if banco_cartas[g][0] == trocas_processamento[a][0]:
            contem_ganhada = True
            break

        else:
            contem_ganhada = False

    #DESEJADA PERDE
    for i in range(0, len(desejadas_cartas)):
        if contem_perdida == True:
            contem_desejada_perde = False
            if desejadas_cartas[i][0] == trocas_processamento[a][1]:
                contem_desejada_perde = True
                break
        
        else:
            contem_desejada_perde = False
            break

    for i in range(0, len(desejadas_cartas)):
        if contem_ganhada == True:
            contem_desejada_ganha = False
            if desejadas_cartas[i][0] == trocas_processamento[a][0]:
                contem_desejada_ganha = True
                break
        else:
            contem_desejada_ganha = False
            break


    if contem_perdida == True:
        #SEM APPEND 
        if contem_ganhada == True:
            if contem_desejada_perde == False: 
                for g in range(0, len(banco_cartas)):
                    if banco_cartas[g][0] == trocas_processamento[a][1]:
                        if int(banco_cartas[g][1]) == 0:
                            print('TROCA NÃO REALIZADA!')
                            break

                        if int(banco_cartas[g][1]) > 0:
                            banco_cartas[g][1] = int(banco_cartas[g][1]) - 1
                            for h in range(0, len(banco_cartas)):
                                if banco_cartas[h][0] == trocas_processamento[a][0]:
                                    banco_cartas[h][1] = int(banco_cartas[h][1]) + 1
                                    print('TROCA REALIZADA!')
                                    break
                
                        
            elif contem_desejada_perde == True:
                for g in range(0, len(banco_cartas)):
                    if banco_cartas[g][0] == trocas_processamento[a][1]:
                        if int(banco_cartas[g][1]) == 0:
                            print('TROCA NÃO REALIZADA!')
                            break

                        if int(banco_cartas[g][1]) > 0:
                            for u in range(0, len(desejadas_cartas)):  
                                if  int(desejadas_cartas[u][1]) >= int(banco_cartas[g][1]) and desejadas_cartas[u][0] == trocas_processamento[a][1]:
                                    print('TROCA NÃO REALIZADA!')
                                    break

                                if int(desejadas_cartas[u][1]) < int(banco_cartas[g][1]) and desejadas_cartas[u][0] == trocas_processamento[a][1]:
                                    banco_cartas[g][1] = int(banco_cartas[g][1]) - 1
                                    for h in range(0, len(banco_cartas)):
                                        if banco_cartas[h][0] == trocas_processamento[a][0]:
                                            banco_cartas[h][1] = int(banco_cartas[h][1]) + 1
                                            print('TROCA REALIZADA!')
                                            break
                                    break
                

        #COM APPEND
        elif contem_ganhada == False:
            if contem_desejada_perde == False: 
                for g in range(0, len(banco_cartas)):
                    if banco_cartas[g][0] == trocas_processamento[a][1]:
                        if int(banco_cartas[g][1]) == 0:
                            print('TROCA NÃO REALIZADA!')
                            break

                        if int(banco_cartas[g][1]) > 0:
                            banco_cartas[g][1] = int(banco_cartas[g][1]) - 1
                            processamento = trocas_processamento[a][0] + ' 1'
                            banco_cartas.append(processamento.split())
                            print('TROCA REALIZADA!')
                            break
                
                
                        
            elif contem_desejada_perde == True:
                for g in range(0, len(banco_cartas)):
                    if banco_cartas[g][0] == trocas_processamento[a][1]:
                        if int(banco_cartas[g][1]) == 0:
                            print('TROCA NÃO REALIZADA!')
                            break

                        if int(banco_cartas[g][1]) > 0:
                            for u in range(0, len(desejadas_cartas)):  
                                if  int(desejadas_cartas[u][1]) >= int(banco_cartas[g][1]) and desejadas_cartas[u][0] == trocas_processamento[a][1]:
                                    print('TROCA NÃO REALIZADA!')
                                    break

                                if int(desejadas_cartas[u][1]) < int(banco_cartas[g][1]) and desejadas_cartas[u][0] == trocas_processamento[a][1]:
                                    banco_cartas[g][1] = int(banco_cartas[g][1]) - 1
                                    processamento = trocas_processamento[a][0] + ' 1'
                                    banco_cartas.append(processamento.split())
                                    print('TROCA REALIZADA!')
                                    break
                
    else:
        print('TROCA NÃO REALIZADA!')
                                

for h in range(0, len(banco_cartas)):
    for g in range(0, len(desejadas_cartas)):
        if banco_cartas[h][0] == desejadas_cartas[g][0]:
            if int(banco_cartas[h][1]) >= int(desejadas_cartas[g][1]):
                desejadas_cartas.remove(desejadas_cartas[g])
                break

if len(desejadas_cartas) == 0:
    print('JOAO CONSEGUIU AS CARTAS DESEJADAS!')
else:
    print('JOAO NAO CONSEGUIU AS CARTAS DESEJADAS!')       
                    

                                        
                                
                           

                        
                                
                        
                                    
                    
        
    

   
        