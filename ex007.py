res = 'y'
while res.lower() == 'y':
    num = input('Type an meter value: ')
    while not num.isdigit():
        num = input('Only numerical values are accepted. Please try again: ')

    num = float(num)
    print('{}m = {}cm\n{}m = {}mm'.format(num, num*100, num, num*1000))

    res = input('\nRun again? (y/n): ')
    print('')
