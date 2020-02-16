res = 'y'
while res.lower() == 'y':
    num = input('Type an number: ')
    while not num.isdigit():
        num = input('Only numerical values are accepted. Please try again: ')

    num = float(num)
    print('\n{} × 2 = {}\n{} × 3 = {}\nSquare Root = {}'.format(num, num * 2, num, num * 3, num ** 0.5))

    res = input('\nRun again? (y/n): ')
    print('')
