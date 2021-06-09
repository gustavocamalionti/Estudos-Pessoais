###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: 
# RA: 
###################################################

# Leitura da matriz

campo = []
for i in range(8):
  campo.append(input().split())

# Leitura e processamento dos sensores

num_sensores = int(input())
alcance = int(input())

for i in range(num_sensores):
  linha, coluna = [int(i) for i in input().split()]
  

# Impressão da saída
print(campo)
print(linha)
print(coluna)