var = input("Digite algo: ")

print('\n')
print('\'{}\' é da classe {}'.format(var, type(var)))
print('É alfanumérico?', var.isalnum())
print('É alfadecimal?',var.isalpha())
print('É decimal?',var.isdecimal())
print('É um digito?',var.isdigit())
print('É um identificador?',var.isidentifier())
print('Está em caixa baixa?',var.islower())
print('Está em caixa alta?',var.isupper())
print('É um valor numérico',var.isnumeric())
print('Pode ser exibido na tela?',var.isprintable())
print('Só possui espaços?',var.isspace())
print('É um título?',var.istitle())