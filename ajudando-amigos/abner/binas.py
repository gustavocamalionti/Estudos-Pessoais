import os
os.getcwd()
os.chdir('C:\\Users\\Gustavo Camalionti\\Documents\\Programação\\cursos-e-tecnologias\\back-end\\estudo-pessoal')
os.getcwd()

man = []
other = []

try:
    data = open('binas.txt', mode = 'r', encoding='utf-8')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            if role == 'Other-Man':
                other.append(line_spoken.strip())
                 
            else:
                man.append(line_spoken.strip())
            
        except:
                pass
    data.close()
except:
    print (' Houve algum problema com o arquivo de dados. Confira a pasta!')

try:
    with open('man_data.txt', 'w') as man_file:
        print(man, file=man_file)
    with open('other_data.txt','w') as other_file:
        print(other, file=other_file)

except IOError:
    print('File error')

print(f'Falas de Abner: {man}')
print(f'Falas de Gustavo: {other}')






