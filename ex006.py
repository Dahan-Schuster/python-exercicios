res = 'y'
while res.lower() == 'y':
    lendo = True
    while (lendo):
        try:
            scr_a = float(input("Type the first student's score: "))
            while scr_a < 0 or scr_a > 10:
                scr_a = float(input('Scores between 0 and 10, please.\nFirst student\'s score: '))

            scr_b = float(input("\nType the second student's score: "))
            while scr_b < 0 or scr_b > 10:
                scr_b = float(input('Scores between 0 and 10, please.\nFirst student\'s score: '))

            lendo = False
        except ValueError:
            print('Only numerical values are accepted. Please try again:\n')

    print('')
    print('Score A: {:>4}\nScore B: {:>4}'.format(scr_a, scr_b))
    print('--------------------------')
    print('Average: {}'.format((scr_a + scr_b) / 2))

    res = input('\nRun again? (y/n): ')
    print('')
