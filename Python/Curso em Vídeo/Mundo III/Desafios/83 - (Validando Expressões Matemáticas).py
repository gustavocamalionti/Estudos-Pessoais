#Desafio 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

#RESOLUÇÃO PESSOAL: Não serve para todos os casos ))) 3*2 ((( expressão inválida
contparent1=0
contparent2=0
expre = str(input(' Escreva uma expressão algébrica usando parênteses: '))

for c in range(0, len(expre)):
    if expre[c]== '(':
        contparent1 = contparent1 + 1
    elif expre[c] == ')':
        contparent2 = contparent2 + 1

if contparent1 == contparent2:
    print('A expressão é válida')
else:
    print('A expressão é inválida')

#RESOLUÇÃO DO PROFESSOR: Tentativa de fazer sozinho após ver a resolução

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

    
    