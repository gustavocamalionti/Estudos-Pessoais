#MUTÁVEIS

lanche = 'Hambúrguer'
lanche = 'Suco'
print(lanche)

#TUPLAS SÃO IMUTÁVEIS
'''lanche[1] = 'Refrigerante' >>>>>> ISSO VAI DAR ERRO
print(lanche)'''

#LIMITES
lanche = 'Hambúrguer','Suco','Pizza','Pudim'
print(lanche[1])
print(lanche[1:3])

#IGUALDADES DE POSIÇÕES E ORIENTAÇÕES
print(lanche[:2])
print(lanche[:-2])
print(lanche[2:])
print(lanche[-2:])

print('-'*25)

print(lanche[1])
print(lanche[1:3])
print(lanche[:2])
print(lanche[:-2])
print(lanche[2:])
print(lanche[-2:])

text = 'LAÇOS DE REPETIÇÔES COM TUPLAS'
print('-'*35)
print(f'{text:^35}')
print('-'*35)

text1 = '1° MÉTODO'
print(f'{text1:^35}')
for c in lanche:
    print(f'Eu vou comer {c}')
print('ACABOU! COMI DEMAIS')

print('-'*35)

text2 = '2° MÉTODO'
print(f'{text2:^35}')
#print(len(lanche))
for cont in range(0,len(lanche)):
    print(lanche[cont])
print('ACABOU! COMI DEMAIS')

print('-'*35)

text3 = '3° MÉTODO'
print(f'{text3:^35}')
for pos, comid in enumerate(lanche):
    print(pos,comid)
    print(f'Eu vou comer {comid} na posição {pos}')
print('ACABOU! COMI DEMAIS')

#USANDO SORTED 
text4 = 'USANDO SORTED'
print('-'*55)
print(f'{text4:^55}')
print('-'*55)

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche)) #ORGANIZADO/EM ORDEM >>>>>>> O PYTHON TRANSFORMOU () EM [], CRIANDO UMA LISTA ORDENADA
print(lanche)


#TUPLAS COM NÚMEROS E OPERAÇÕES
text4 = 'TUPLAS COM NÚMEROS E OPERAÇÕES'
print('-'*55)
print(f'{text4:^55}')
print('-'*55)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #LEMBRAR DE CONJUNTOS NUMÉRICOS/SQN CUIDADO
print(a)
print(b)
print(c) #a + b != b + a

print('-'*55)

c = b + a
print(c)
print(c.count(5)) #CONTADOR DE NUMEROS
print(c.count(4)) 
print(c.count(9))
print(c.index(8)) #POSIÇÃO DO 8
print(c.index(4)) #POSIÇÃO DO 4
print(c.index(2)) #POSIÇÃO DO 2
print(c.index(5, 1)) #COMEÇAR CONTAR '5' APARTIR DA POSIÇÃO 1 >>>>>> RESULTADO: O 5 ESTÁ NA QUINTA POSIÇÃO

#OUTRAS FUNCIONALIDADES
text5 = 'OUTRAS FUNCIONALIDADES'
print('-'*55)
print(f'{text5:^55}')
print('-'*55)

pessoa = ('Gustavo', 21, 'M', 73.5)
print(pessoa)
#del(pessoa) >>>>>>>>>>>>>>>>>> APAGA DA MEMORIA