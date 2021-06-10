###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: 
# RA: 
###################################################

# Leitura da matriz

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
  


for sensor in range(0, len(sensores)):
  for linha in range(0, len(campo)): 
    for coluna in range(0, len(campo)):

      if sensores[sensor][linha] == campo[linha]:
        print(sensores)

#NORTE


#SUL


#LESTE


#OESTE

# Impressão da saída
print(sensores)

