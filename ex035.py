'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

lado1 = float(input("Digite o 1° lado: "))
lado2 = float(input("Digite o 2° lado: "))
lado3 = float(input("Digite o 3° lado: "))

if lado1+lado2 > lado3 and lado2+lado3 > lado1 and lado1+lado3 > lado2:
    resultado = "é" 
else:
    resultado = "não é"    
    
print(f"Com esses lados {resultado} possível formar um triângulo")