###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: 
# RA: 
###################################################

# Leitura da matriz
validacao_sensores = []
sensores = []
campo = []
for i in range(8):
  campo.append(input().split())

# Leitura e processamento dos sensores

num_sensores = int(input())
alcance = int(input())

for i in range(num_sensores):
  transformacao = str(input(''))
  sensores.append(transformacao.split())
  
for a in range(0, len(sensores)):
  while True:
    #NORTE
    for c in range(int(sensores[a][0]) -1, -1, -1):
      print(c)
      if campo[c][int(sensores[a][1])] == 'x':
        transformacao = (f'{c} {sensores[a][1]}').split()
        contem_sensor = False
        for g in range(0, len(validacao_sensores)):
          if validacao_sensores[g] == transformacao:
            contem_sensor == True
        
        if contem_sensor == False:
          print(f'{validacao_sensores} 1')
          validacao_sensores.append(transformacao)

      if campo[c][int(sensores[a][1])] == 'o':
        break


    #SUL
    for c in range(int(sensores[a][0])+1, 8):
      if campo[c][int(sensores[a][1])] == 'x':
        transformacao = (f'{c} {sensores[a][1]}').split()
        contem_sensor = False
        for g in range(0, len(validacao_sensores)):
          if validacao_sensores[g] == transformacao:
            contem_sensor == True
        
        if contem_sensor == False:
          print(sensores[a])
          print(f'testando {c} {sensores[a][1]}')
          print(f'{validacao_sensores} 2')
          validacao_sensores.append(transformacao)

      if campo[c][int(sensores[a][1])] == 'o':
        break
    

    #LESTE
    for c in range(int(sensores[a][1])+1, 8):
      if campo[int(sensores[a][0])][c] == 'x':
        transformacao = (f'{sensores[a][0]} {c}').split()
        contem_sensor = False
        for g in range(0, len(validacao_sensores)):
          if validacao_sensores[g] == transformacao:
            contem_sensor == True
        
        if contem_sensor == False:
          print(f'{validacao_sensores} 3')
          validacao_sensores.append(transformacao)

      if campo[int(sensores[a][0])][c] == 'o':
        break

    #OESTE
    for c in range(int(sensores[a][1])-1, -1, -1):
      if campo[int(sensores[a][0])][c] == 'x':
        transformacao = (f'{sensores[a][0]} {c}').split()
        contem_sensor = False
        for g in range(0, len(validacao_sensores)):
          if validacao_sensores[g] == transformacao:
            contem_sensor == True
        
        if contem_sensor == False:
          print(f'{validacao_sensores} 4')
          validacao_sensores.append(transformacao)

      if campo[int(sensores[a][0])][c] == 'o':
        break

    break

print(validacao_sensores)
if len(validacao_sensores) == 0:
  print('Nenhum bau encontrado.')

else:
  print(f'{len(validacao_sensores)} bau(s) encontrado(s).')

