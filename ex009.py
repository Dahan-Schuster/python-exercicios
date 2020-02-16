res = 's'
while res.lower() == 's':
    a = float(input('Conversor real-dólar.\n\nDigite um valor em reais: '))

    print('R${0:.2f} podem comprar US${1:.2f}'.format(a, (a/3.27)))

    res = input("Deseja converter novamente? (s/n)")
    print('')
