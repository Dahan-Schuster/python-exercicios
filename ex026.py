nome = input('Digite seu nome completo: ')
nome_dividido = nome.split()

print('Primeiro nome:', nome_dividido[0])
print('Último nome:', nome_dividido[len(nome_dividido) - 1])