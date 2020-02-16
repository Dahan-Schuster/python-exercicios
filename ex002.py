lendo = True
while(lendo):
    try:
        a = int(input("A: "))
        b = int(input("B: "))
        lendo = False
    except ValueError:
        print('Digite apenas números.\n')

s = a + b
print('\nA soma entre {} e {} vale {} '.format(a, b, s))
