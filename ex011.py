res = 's'
while res.lower() == 's':
    preco = input('Digite o valor original: ')
    while not preco.isdigit():
        preco = input('Apenas valores numéricos são permitidos. Tente novamente: ')

    preco = float(preco)
    novo_preco = preco * 0.95
    print('{0:0.2f} com 5% de desconto: {1:0.2f}'.format(preco, novo_preco))

    res = input("\nDeseja calcular novamente? (s/n)")
    print('')
