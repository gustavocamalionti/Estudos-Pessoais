#Desafio 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

#RESOLUÇÃO PESSOAL
expressao_numerica = str(input('Digite uma expressão numérica com parênteses '))

lista_parenteses = []

for c in range(0,len(expressao_numerica)): 
    if expressao_numerica[c] == '(':
        lista_parenteses.append('(')
        print('Teste')
    elif expressao_numerica[c] == ')':
        if len(lista_parenteses) > 0:
            lista_parenteses.pop()
            print('teste')
        elif len(lista_parenteses) == 0:
            lista_parenteses.append(')')
            break
    
if len(lista_parenteses) == 0:
    print(f'A expressão é válida')
    
else:
    print(f'A expressão é inválida')
        
#RESOLUÇÃO DO PROFESSOR

expre = str(input(' Escreva uma expressão algébrica usando parênteses: '))
pilha = []

for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')


        
    
    