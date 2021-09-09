# Faça um programa em Python que solicite a quantidade de alunos de uma turma. 

# Após esta informação, o usuário deve digitar a média de cada aluno da turma, e o programa apresentará a mensagem PARABÉNS, VOCÊ ESTÁ APROVADO aos alunos com média maior ou igual a 6,.0. 

# O programa deve calcular e mostrar, no final da entrada de dados, a média geral da turma.

# Obs.: Caso a quantidade informada de alunos da turma for igual a zero, o programa deve emitir a seguinte mensagem: NÃO HOUVE PROCESSAMENTO

somador_para_media = 0
lista_notas_alunos = []
quantidade_alunos = int(input(''))

for c in range(0, quantidade_alunos):
    lista_notas_alunos.append(float(input('')))
    somador_para_media = somador_para_media + float(lista_notas_alunos[c])
    
for c in range(len(lista_notas_alunos)):
    if float(lista_notas_alunos[c]) >= 6:
        print("PARABÉNS VOCÊ ESTÁ APROVADO")

if quantidade_alunos == 0:
    print('NÃO HOUVE PROCESSAMENTO')

else:
    print(somador_para_media/quantidade_alunos)
