'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input("Digite o seu salário atual: "))

if salario <= 1250:
    aumento = 1.15
else:
    aumento = 1.1

novo_salario = salario*aumento

print(f"Seu novo salário será R${novo_salario}")