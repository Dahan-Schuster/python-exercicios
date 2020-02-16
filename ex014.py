dias = float(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos kilômetros foram rodados com o carro? '))

total_a_pagar = dias * 60 + km * 0.15

print('\nO valor total a pagar é R${:.2f}'.format(total_a_pagar))