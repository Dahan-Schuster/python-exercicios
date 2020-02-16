res = 's'
while res.lower() == 's':
    lendo = True
    while lendo:
        try:
            num = int(input('Digite um número: '))
            lendo = False
        except ValueError:
            print('Apenas valores numéricos.')

    print('Tabuada de {}:'.format(num))
    print('+-----------------+')
    print('| {0} * 1  =  {1:5d} |'.format(num, num))
    print('| {0} * 2  =  {1:5d} |'.format(num, num * 2))
    print('| {0} * 3  =  {1:5d} |'.format(num, num * 3))
    print('| {0} * 4  =  {1:5d} |'.format(num, num * 4))
    print('| {0} * 5  =  {1:5d} |'.format(num, num * 5))
    print('| {0} * 6  =  {1:5d} |'.format(num, num * 6))
    print('| {0} * 7  =  {1:5d} |'.format(num, num * 7))
    print('| {0} * 8  =  {1:5d} |'.format(num, num * 8))
    print('| {0} * 9  =  {1:5d} |'.format(num, num * 9))
    print('| {0} * 10 =  {1:5d} |'.format(num, num * 10))
    print('+-----------------+')

    res = input('\nCalcular novamente? (s/n): ')
    print('')

s