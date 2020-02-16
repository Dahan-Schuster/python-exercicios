nota_1 = float(input('Digite a primeira nota do aluno (Utilize ponto se necessário): '))
while nota_1 < 0 or nota_1 > 10:
    nota_1 = float(input('Apenas valores entre 0 e 10. Tente novamente (Utilize ponto se necessário): '))

nota_2 = float(input('Digite a primeira nota do aluno (Utilize ponto se necessário): '))
while nota_2 < 0 or nota_2 > 10:
    nota_2 = float(input('Apenas valores entre 0 e 10. Tente novamente (Utilize ponto se necessário): '))

media = (nota_1 + nota_2) / 2

print('')
if media < 5.0:
    print('REPROVADO', end=' ')
else:
    print('RECUPERAÇÃO', end=' ') if media < 7 else print('APROVADO', end=' ')

print('com média {:.2f}'.format(media))