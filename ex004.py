res = 'y'
while res.lower() == 'y':
    num = input('Type an integer number: ')
    while not num.isdigit():
        num = input('Only numerical values are accepted. Please try again: ')

    num = int(num)
    print('\n{} < {} < {}'.format(num-1, num, num+1))
    res = input('\nRun again? (y/n): ')
    print('')

