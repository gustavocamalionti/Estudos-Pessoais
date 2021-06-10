#EXEMPLO DE ENTRADAS
#. . . . . . . .
#. . . . . . . .
#. . . x . . . .
#. . . . . . . .
#. . . . . . . .
#. . . . . . . .
#. . . . . . . .
#. . . . . . . .
#1
#2
#4 3

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
    cont = 0
    for c in range(int(sensores[a][0]) -1, -1, -1):
      cont = cont + 1
      if campo[c][int(sensores[a][1])] == 'o' or cont > alcance:
        break

      if campo[c][int(sensores[a][1])] == 'x':
        transformacao = (f'{c} {sensores[a][1]}').split()
        contem_sensor = False
        for g in range(0, len(validacao_sensores)):
          if validacao_sensores[g] == transformacao:
            contem_sensor = True
        
        if contem_sensor == False:
          validacao_sensores.append(transformacao)

    #SUL
    cont = 0
    for c in range(int(sensores[a][0]), 8):
      cont = cont + 1
      if campo[c][int(sensores[a][1])] == 'o' or cont > alcance:
        break

      if campo[c][int(sensores[a][1])] == 'x':
        transformacao = (f'{c} {sensores[a][1]}').split()
        contem_sensor = False
        for g in range(0, len(validacao_sensores)):
          if validacao_sensores[g][0] == transformacao[0] and validacao_sensores[g][1] == transformacao[1]:
            contem_sensor = True
            break
        if contem_sensor == False:
          validacao_sensores.append(transformacao)
          

    

    #LESTE
    cont = 0
    for c in range(int(sensores[a][1]), 8):
      cont = cont + 1
      if campo[int(sensores[a][0])][c] == 'o' or cont > alcance:
        break

      if campo[int(sensores[a][0])][c] == 'x':
        transformacao = (f'{sensores[a][0]} {c}').split()
        contem_sensor = False
        for g in range(0, len(validacao_sensores)):
          if validacao_sensores[g][0] == transformacao[0] and validacao_sensores[g][1] == transformacao[1]:
            contem_sensor = True
            break
        
        if contem_sensor == False:
          validacao_sensores.append(transformacao)
          



    #OESTE
    cont = 0
    for c in range(int(sensores[a][1]), -1, -1):
      cont = cont + 1
      if campo[int(sensores[a][0])][c] == 'o' or cont > alcance:
        break

      if campo[int(sensores[a][0])][c] == 'x':
        transformacao = (f'{sensores[a][0]} {c}').split()
        contem_sensor = False
        for g in range(0, len(validacao_sensores)):
          if validacao_sensores[g][0] == transformacao[0] and validacao_sensores[g][1] == transformacao[1]:
            contem_sensor = True
            break
        
        if contem_sensor == False:
          validacao_sensores.append(transformacao)
          
    break

if len(validacao_sensores) == 0:
  print('Nenhum bau encontrado.')

else:
  print(f'{len(validacao_sensores)} bau(s) encontrado(s).')

