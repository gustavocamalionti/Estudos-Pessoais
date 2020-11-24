#Desafio 85: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. 


#RESOLUÇÃO PESSOAL
valores_paridade = [[], []]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor%2 == 0:
        if len(valores_paridade[0]) == 0: #Primeiro Valor
            valores_paridade[0].append(valor)

        elif valor>max(valores_paridade[0]): #Ultimo valor
            valores_paridade[0].append(valor)
        
        else:
            pos = 0
            while pos < len(valores_paridade[0]):
                if valor <= valores_paridade[0][pos]:
                    valores_paridade[0].insert(pos, valor)
                    break
                pos += 1
    
    else:
        if len(valores_paridade[1]) == 0: #adicionar o primeiro valor par
            valores_paridade[1].append(valor)

        elif valor>max(valores_paridade[1]): #Adicionar o maior valor impar
            valores_paridade[1].append(valor)
        
        else:
            pos = 0 
            while pos < len(valores_paridade[1]):
                if valor <= valores_paridade[1][pos]:
                    valores_paridade[1].insert(pos, valor)
                    break
                pos += 1

print(f'Os valores pares digitados foram: {valores_paridade[0]} ')
print(f'Os valores impares digitados foram: {valores_paridade[1]}')

