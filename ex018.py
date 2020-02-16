from random import randint
alunos = [input('Primeiro aluno: '), input('Segundo aluno: '), input('Terceiro aluno: '), input('Quarto aluno: ')]
print('\n{} foi sorteado para apagar o quadro.'.format(alunos[randint(0, 3)]))