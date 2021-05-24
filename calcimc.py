#Calculo IMC
import time
time.sleep(1.05)
print('Olá, através deste programa você podera calcular o seu Índice de Massa Corporal.')
nome = str(input('Nos diga seu nome: '))
altura = float(input(f'Olá {nome}, por favor, digite sua altura em metros: '))
peso = float(input('Ok, agora digite seu peso em quilos: '))
imc = peso/altura ** 2
print(f'Seu IMC é {imc:.4f}')
if imc < 16:
    print('Magreza Grave')
elif imc < 17:
    print('Magreza Moderada')
elif imc < 18.5:
    print('Magreza Leve')
elif imc < 25:
    print('Saudável')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade Grau 1 ')
elif imc < 40:
    print('Obesidade Grau 2 (Severa) ')
else:
    print('Obesidade Grau 3 (Muito Grave) ')
time.sleep(1.5)
print('Espero que tenha ajudado :) ')
fim = input('Pressione Enter para sair: ')