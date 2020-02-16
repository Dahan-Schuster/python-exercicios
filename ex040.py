idade = int(input('Digite a idade do atleta: '))
while idade < 1 or idade > 130:
    idade = int(input('Digite uma idade válida: '))

print('\nO atleta é da categoria \033[30;46m ', end='')

if idade <= 9:
    print('MIRIM \033[m')
elif idade <= 14:
    print('INFANTIL \033[m')
elif idade <= 19:
    print('JUNIOR \033[m')
elif idade == 20:
    print('SÊNIOR \033[m')
else:
    print('MASTER \033[m')
