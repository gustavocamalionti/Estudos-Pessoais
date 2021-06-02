#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Magic: Trocando Cartas
# Nome: 
# RA: 
#####################################################


banco_cartas = list()
desejadas_cartas = list()
trocas_processamento = list()

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

for c in range(0, len(trocas_processamento)):
    for z in range(0, len(banco_cartas)):
        for t in range(0,len(desejadas_cartas)):
            contem_carta = False

            #TROCA REALIZADA
            if (trocas_processamento[c][1] == banco_cartas[z][0]) and (int(banco_cartas[z][1]) > 0):
                #CARTA PERDIDA
                for t in range(0, len(desejadas_cartas)):
                    if (banco_cartas[z][0] == desejadas_cartas[t][0]) and (int(banco_cartas[z][1]) <= int(desejadas_cartas[t][1])):
                        print('1')
                        print('TROCA NÃO REALIZADA')

                    
                    elif (banco_cartas[z][0] == desejadas_cartas[t][0]) and (int(banco_cartas[z][1]) > int(desejadas_cartas[t][1])):
                        banco_cartas[z][1] = int(banco_cartas[z][1]) - 1
                        for t in range(0, len(banco_cartas)):
                            if trocas_processamento[c][0] == banco_cartas[t][0]:
                                contem_carta = True
                        
                        if contem_carta == True:
                            banco_cartas[t][1] = int(banco_cartas[t][1]) + 1
                            print('2')
                            print('TROCA REALIZADA')
                        
                        else:
                            processamento2 = trocas_processamento[c][0] + ' 1' 
                            banco_cartas.append(processamento2.split())
                            print('3')
                            print('TROCA REALIZADA')

                        

                    
                    else:
                        contem_carta = False
                        banco_cartas[z][1] = int(banco_cartas[z][1]) - 1

                        #CARTA GANHADA
                        for t in range(0, len(banco_cartas)):
                            if trocas_processamento[c][0] == banco_cartas[t][0]:
                                contem_carta = True
                                
                        
                        if contem_carta == True:
                            banco_cartas[t][1] = int(banco_cartas[t][1]) + 1
                            print('4')
                            print('TROCA REALIZADA')
                        
                        else:
                            processamento2 = trocas_processamento[c][0] + ' 1' 
                            banco_cartas.append(processamento2.split())
                            print('5')
                            print('TROCA REALIZADA')

                        
            
            #TROCA NÃO REALIZADA
            elif (trocas_processamento[c][1] == banco_cartas[z][0]) and (int(banco_cartas[z][1]) <= 0):
                print('6')
                print('TROCA NÃO REALIZADA')

            
        #TROCA NÃO REALIZADA

print(f'Cartas no banco: {banco_cartas}')
print(f'Cartas desejadas: {desejadas_cartas}')
print(trocas_processamento)
