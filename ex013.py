#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


salarioBruto = float(input("Qual o seu salrário atual?\n->R$"))
acrescimo = 1.15 #equivale a um acrescimo de 15%

salarioAcrescido = salarioBruto*acrescimo

print(f"R${salarioBruto} + 15% = {salarioAcrescido :.2f}")

