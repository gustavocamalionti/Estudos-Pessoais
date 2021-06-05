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
        
        if contem_perdida == True:
            #SEM APPEND 
            if contem_ganhada == True:
                    #PARA REALIZAR
                    for g in range(len(banco_cartas)):
                        if banco_cartas[g][0] == trocas_processamento[a][1] and int(banco_cartas[g][1]) >= 0 and contem_desejada_perde == False:
                            banco_cartas[g][1] = int(banco_cartas[g][1]) - 1
                            for h in range(len(banco_cartas)):
                                if banco_cartas[h][0] == trocas_processamento[a][0]:
                                    banco_cartas[h][1] = int(banco_cartas[h][1]) + 1
                                    print(banco_cartas)
                                    print('TROCA REALIZADA 1')
                                    break
                            break
                        
            
                        if banco_cartas[g][0] == trocas_processamento[a][1] and int(banco_cartas[g][1]) >= 0 and contem_desejada_perde == True:
                            for h in range(0, len(desejadas_cartas)):
                                 if desejadas_cartas[h][0] == trocas_processamento[a][0] and int(desejadas_cartas[h][1]) < int(banco_cartas[g][1]):
                                    banco_cartas[g][1] = int(banco_cartas[g][1]) - 1
                                    for t in range(len(banco_cartas)):
                                        if banco_cartas[t][0] == trocas_processamento[a][0]:
                                            banco_cartas[t][1] = int(banco_cartas[t][1]) + 1
                                            print('TROCA REALIZADA 2')
                                            break
                                    break
                            
                                

                        if banco_cartas[g][0] == trocas_processamento[a][1] and int(banco_cartas[g][1]) >= 0 and contem_desejada_perde == True:
                            for h in range(0, len(desejadas_cartas)):
                                 if desejadas_cartas[h][0] == trocas_processamento[a][0] and int(desejadas_cartas[h][1]) >= int(banco_cartas[g][1]):
                                    banco_cartas[g][1] = int(banco_cartas[g][1]) - 1
                                    for h in range(len(banco_cartas)):
                                        if banco_cartas[h][0] == trocas_processamento[a][0]:
                                            banco_cartas[g][1] = int(banco_cartas[g][1]) + 1
                                            print('TROCA NÃO REALIZADA 3')
                                            break
                                    break
                                        
                            break
                        

                                
                    #PARA NÃO REALIZAR
                    for g in range(len(banco_cartas)):
                        if banco_cartas[g][0] == trocas_processamento[a][1] and int(banco_cartas[g][1]) < 0:
                        
                            print('TROCA NÃO REALIZADA 4')
                            break
                    break
                            
                

            #COM APPEND
            elif contem_ganhada == False:
                if contem_desejada_perde == False: 
                    for g in range(0, len(banco_cartas)):
                        if trocas_processamento[a][1] == banco_cartas[g][0]:
                            for u in range(0, len(banco_cartas)):
                                if int(banco_cartas[u][1]) > 0:
                                    banco_cartas[g][1] = int(banco_cartas[g][1]) - 1
                                    processamento = trocas_processamento[a][0] + ' 1'
                                    banco_cartas.append(processamento.split())
                                    print(banco_cartas)
                                    print('TROCA REALIZADA 5')
                                    break
                            break    
                        break
                if contem_desejada_perde == True:
                    for g in range(0, len(desejadas_cartas)):
                        if trocas_processamento[a][1] == desejadas_cartas[g][0]:
                            for u in range(0, len(banco_cartas)):
                                if int(banco_cartas[u][1]) > int(desejadas_cartas[g][1]):
                                    banco_cartas[u][1] = int(banco_cartas[u][1]) - 1
                                    processamento = trocas_processamento[a][0] + ' 1'
                                    banco_cartas.append(processamento.split())
                                    print(banco_cartas)
                                    print('TROCA REALIZADA 6')
                                    break

                                if int(banco_cartas[u][1]) <= int(desejadas_cartas[g][1]):
                                    print(banco_cartas)
                                    print('TROCA NÃO REALIZADA 9')
                                    break

                                


                        break            
            

        
        else:
            print('TROCA NÃO REALIZADA 9')
            break




print(f'COMBINAÇÃO {trocas_processamento[a]} ||| contem_ganhada: {contem_ganhada} >> contem_ perdida: {contem_perdida} ||| contem_desejada_ganha: {contem_desejada_ganha} ||| contem_desejada_perde {contem_desejada_perde}')
print(banco_cartas)