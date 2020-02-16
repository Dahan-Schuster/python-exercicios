tabuada = abs(int(input('Informe a tabuada desejada: ')))

print('+-------------+')
for multiplicador in range(1, 11):
    resultado = tabuada * multiplicador
    print('| {} * {:02d} = {:02d} |'.format(tabuada, multiplicador, resultado))
print('+-------------+')