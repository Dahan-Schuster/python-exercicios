res = 's'
while res.upper() == 'S':
    ano = int(input('\nDigite um ano: '))
    print('{} é um ano bissexto'.format(ano)) if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else print('{} é um ano comum.'.format(ano))
    res = str(input('Deseja calcular novamente?(S/n): '))
