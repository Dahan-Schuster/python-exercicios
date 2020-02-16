from random import randint
alunos = []
for i in range(0, int(input('Quantidade de alunos: '))):
    alunos.append(input('{}° aluno: '.format(i+1)))
print('\nOrdem de aprensentação:')
while len(alunos) > 0:
    random_index = randint(0, len(alunos)-1)
    print(' >> ', end='')
    print(alunos[random_index], end='')
    alunos.pop(random_index)
