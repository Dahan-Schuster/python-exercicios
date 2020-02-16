peso = float(input('Digite seu peso (kg): '))
while peso < 1:
    peso = float(input('Digite um peso válido (kg): '))
altura = int(input('Digite sua altura (cm): ')) / 100
while altura < 1:
    altura = int(input('Digite uma altura válida (cm): ')) / 100

imc = peso / altura**2

print('\n\033[1;36mImc: {:.2f}\033[m\n'.format(imc))

if imc < 18.5:
    print('\033[31mVocê está Abaixo do peso.\033[m')
elif imc < 25:
    print('\033[32mSeu peso está Ideal.\033[m')
elif imc < 30:
    print('\033[33mVocê está com Sobrepeso.\033[m')
elif imc < 40:
    print('\033[31mVocê é Obeso.\033[m')
else:
    print('\033[1;4;31mVocê possui Obesidade Mórbida.\033[m')
