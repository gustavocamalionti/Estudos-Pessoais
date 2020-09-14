#DESAFIO 71V2: usando a mesma ideia do Desafio 71, considere as notas de 100, 50, 20, 10 e 1. Onde há um número limitado de notas no caixa eletrônico (você pode defini-las).

caixa = 'CAIXA ELETRÔNICO'
print('-'*37)
print(f'{caixa:^37}')
print('-'*37)

estoque = True
estoque50 = 10
estoque20 = 10
estoque10 = 10
estoque1 = 10
somaestoque = estoque50*50 + estoque20*20 + estoque10*10 + estoque1*1
while estoque is True:
    saque = int(input('Qual será o valor de saque? R$'))
    if somaestoque<saque:
        estoque = False
    else: 
        total = saque 
        céd = 50
        totcéd = 0
        

        while True:
            if total >= céd:
                total = total - céd
                totcéd = totcéd + 1
            else:
                if totcéd>0: 
                    print(f'Total de {totcéd} cédulas de R${céd:.2f}')
                if céd == 50:
                    céd = 20
                    estoque50 = estoque50 - totcéd
                elif céd == 20:
                    céd = 10
                    estoque20 = estoque20 - totcéd
                elif céd == 10:
                    céd = 1
                    estoque10 = estoque10 - totcéd
                elif céd == 1:
                    estoque1 = estoque1 - totcéd
                if total == 0:
                    break
                totcéd = 0
                somaestoque = estoque50*50 + estoque20*20 + estoque10*10 + estoque1*1
        print('\033[32mSAQUE REALIZADO COM SUCESSO!!!\033[m Agradecemos a preferência.')
        print(f'{somaestoque} soma total')
        print(f'{estoque50} estoque 50')
        print(f'{estoque20} estoque 20')
        print(f'{estoque10} estoque 10')
        print(f'{estoque1} estoque 1')

print('\033[31mFALHA NO SAQUE. CÉDULAS INSUFICIENTES!\033[m')

#OUTRA RESOLUÇÃO: ESTUDAR
'''nota5 = 5
nota10 = 10
nota20 = 20
nota50 = 50

qtdNota5 = 10
qtdNota10 = 10
qtdNota20 = 10
qtdNota50 = 10

valMaxSacar = qtdNota5*(nota5 + nota10 + nota20 + nota50)

qt5usada = 0
qt10usada = 0
qt20usada = 0
qt50usada = 0

while(True):
    sac = int(input('Digite o valor que deseja sacar: ')) #não estou fazendo tratamento de erros

    if(sac <= valMaxSacar):

        if(sac%5 == 0):
            
            if(sac//nota50 <=qtdNota50):
                qt50usada = sac//nota50
                
            else:
                qt50usada = qtdNota50

            sac = sac - nota50*qt50usada
            

            if(sac != 0):
                
                if(sac//nota20 <=qtdNota20):
                    qt20usada = sac//nota20
                else:
                    qt20usada = qtdNota20

                sac = sac - nota20*qt20usada
                

            if(sac != 0):
                if(sac//nota10 <=qtdNota10):
                    qt10usada = sac//nota10
                else:
                    qt10usada = qtdNota10

                sac = sac - nota10*qt10usada
                

            if(sac != 0):
                if(sac//nota5 <=qtdNota5):
                    qt5usada = sac//nota5
                else:
                    qt5usada = qtdNota5

                sac = sac - nota5*qt5usada

            break

        else:
            print('Valor não é multiplo de 5')

    else:
        print('Valor ultrapassou o limite de caixa')
                
print('Foram usadas: ',qt50usada,'notas de 50')
print(qt20usada,'notas de 20')
print(qt10usada,'notas de 10')
print(qt5usada,'notas de 5')'''