celsius = float(input('Digite a temperatura em graus Celsius (°C): '))

fahrenheit = (celsius * (9 / 5)) + 32

print('{:.1f}°C correspondem a {:.1f}°F'.format(celsius, fahrenheit))