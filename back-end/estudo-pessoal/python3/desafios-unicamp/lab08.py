#EXEMPLO DE ENTRADAS
#8
#Poeminho do contra

#Todos esses que ai estao
#Atravancando meu caminho,
#Eles passarao...
#Eu passarinho!

#Mario Quintana
#marca

palavras = list()
linha = list()
cont = 0
cont2 = 0

numerolinhas = int(input());
for c in range(0,numerolinhas):
    linha.append(input().lower().split())
    if len(linha[c+cont]) == 0:
        cont = cont - 1
        linha.pop()

for z in range(0, len(linha)):
    for y in range(0, len(linha[z])):
        palavras.append(linha[z][y])

        if linha[z][y] == '.,:;!?':
            palavras.pop()

palavrabusca = list(str((input()).lower()))
cont4=0

afirmacao = 0
resultados = list()
for t in range(0,len(palavras)): 
    for h in range(0, len(palavras[t])):
        if len(palavrabusca) == 0:
            break

        if palavrabusca[0] == palavras[t][h]:                           
            resultados.append(f'{palavras[t][h]}{palavras.index(palavras[t])+1}{palavras[t].index(palavras[t][h])+1}')
            palavrabusca.pop(0)
            break

#PRINT
if len(palavrabusca) != 0:
    print('Palavra não encontrada')

else:
    print('Palavra encontrada')
    for c in range(0, len(resultados)):
        print(f'{resultados[c][0]}: palavra {resultados[c][1]}, letra {resultados[c][2]}')
