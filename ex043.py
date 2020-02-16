preco_normal = float(input('Informe o \033[1;33mpreço da compra:\033[m '))

pagamento = input('Informe a \033[1;33mcondição de pagamento\033[m:\n'
                  '[1]........À vista (\033[1;36mdinheiro/cheque\033[m)\n'
                  '[2]........À vista (\033[1;36mcartão\033[m)\n'
                  '[3]........Até \033[1;36m2x no cartão\033[m\n'
                  '[4]........\033[1;36m3x ou mais\033[m no cartão\n'
                  '\n--> ')

while pagamento != '1' and pagamento != '2' and pagamento != '3' and pagamento != '4':
    pagamento = input('Escolha um opção válida.\n\n--> ')

if pagamento == '1':
    novo_preco = preco_normal * 0.90
    print('Desconto de \033[32m10%\033[m')
elif pagamento == '2':
    novo_preco = preco_normal * 0.95
    print('Desconto de \033[32m15%\033[m')
elif pagamento == '3':
    novo_preco = preco_normal * 1.00
    parcela = novo_preco / 2
    print('\nCada parcela irá custar \033[1;32mR${:.2f}\033[m sem juros.'.format(parcela))
elif pagamento == '4':
    novo_preco = preco_normal * 1.20
    quantidade_parcelas = int(input('Informe a \033[33mquantidade de parcelas\033[m: '))
    while quantidade_parcelas < 3:
        quantidade_parcelas = int(input('Mínimo de 3 parcelas para a opção escolhida: '))
    parcela = novo_preco / quantidade_parcelas
    print('\nCada parcela irá custar \033[1;32mR${:.2f}\033[m com juros de 20%'.format(parcela))

print('Preço a ser pago de acordo com a opão escolhida: \033[1;32mR${:.2f}\033[m'.format(novo_preco))