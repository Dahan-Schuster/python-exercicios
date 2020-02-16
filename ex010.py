res = 's'
while res.lower() == 's':
    lar = input('Digite a largura da parede: ')
    while not lar.isdigit():
        lar = input('Apenas valores numéricos são permitidos. Tente a largura novamente: ')

    alt = input('Digite a altura da parede: ')
    while not lar.isdigit():
        alt = input('Apenas valores numéricos são permitidos. Digite a altura novamente: ')

    alt = float(alt)
    lar = float(lar)

    area = (lar*alt)
    print('\nÁrea da parede em metros quadrados: {0:.2f}m²'.format(area))
    print('Quantidade de tinta necessária em litros: {}l'.format(area / 2))

    res = input("\nDeseja calcular novamente? (s/n)")
    print('')
