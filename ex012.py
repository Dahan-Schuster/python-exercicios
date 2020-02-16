res = 's'
while res.lower() == 's':
    valor = input('Digite o salário original: ')
    while not valor.isdigit():
        valor = input('Apenas valores numéricos são permitidos. Tente novamente: ')

    valor = float(valor)
    novo_valor = valor * 1.15
    print('{0:0.2f} com 15% de aumento: {1:0.2f}'.format(valor, novo_valor))

    res = input("\nDeseja calcular novamente? (s/n)")
    print('')